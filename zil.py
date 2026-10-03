#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kapi Zili Itiraz Komisyonu.

Zil, kurul karar vermeden calmaz. Bu bir bug degil, ic tuzuktur.
"""

from __future__ import annotations

import argparse
import base64
import json
import random
import sys
from datetime import datetime
from pathlib import Path

KOMISYON = ("Baskan Zil", "Raportor Zil", "Muhalefet Zili")
SINIFLAR = (
    "kargo",
    "komsu",
    "tanidik olmayan dayi",
    "sadece ruzgar",
    "kapici",
    "yanlis kat",
    "felsefe ogrencisi",
    "sessizlige itiraz eden biri",
)


def muhur_coz(paket: dict) -> str:
    ham = paket.get("arsiv_muhuru", "")
    try:
        return base64.b64decode(ham).decode("utf-8")
    except Exception:
        return "muhur okunamadi, komisyon tatilde"


def karar_ver(ziyaretci: str, kat: int, saat: str) -> dict:
    saat_parca = saat.split(":")
    saat_sayi = int(saat_parca[0]) if saat_parca and saat_parca[0].isdigit() else 12
    sinif = ziyaretci.strip().lower() or random.choice(SINIFLAR)
    gece = saat_sayi >= 22 or saat_sayi < 7
    supheli = any(k in sinif for k in ("dayi", "felsefe", "yanlis", "ruzgar"))

    if gece and "kargo" in sinif:
        hukum = "RET"
        gerekce = "Gece kargosu kargo degil, kapinin ruyasidir. Zil susar."
        sure_ms = 0
    elif kat <= 0:
        hukum = "YETKISIZLIK"
        gerekce = "Bodrum komisyonun yetki alaninda degil. Orada zil degil, nem konusur."
        sure_ms = 0
    elif supheli:
        hukum = "SERHLI KABUL"
        gerekce = "Ziyaretci supheli ama kapida bekliyor. Bir kisa calma, uc uzun tutanak."
        sure_ms = 180
    else:
        hukum = "KABUL"
        gerekce = "Ziyaretci dosyaya uygundur. Zil, utanarak bir kez calabilir."
        sure_ms = 420 if kat < 5 else 900

    oylar = {
        "Baskan Zil": hukum,
        "Raportor Zil": "TUTANAK TUTULDU",
        "Muhalefet Zili": "SERH: karara karsi degilim, kararin varligina karsi degilim, sadece zilin sesine karsiim",
    }
    dosya_no = f"ZIL-{datetime.now().strftime('%Y%m%d')}-{kat:02d}-{random.randint(100, 999)}"
    return {
        "dosya_no": dosya_no,
        "ziyaretci": sinif,
        "kat": kat,
        "saat": saat,
        "hukum": hukum,
        "gerekce": gerekce,
        "calma_ms": sure_ms,
        "oylar": oylar,
        "uye_sayisi": len(KOMISYON),
    }


def tutanak_yaz(karar: dict, gizli: str) -> Path:
    klasor = Path("tutanaklar")
    klasor.mkdir(exist_ok=True)
    yol = klasor / f"{karar['dosya_no']}.txt"
    metin = "\n".join(
        [
            "KAPI ZILI ITIRAZ KOMISYONU TUTANAGI",
            "=" * 42,
            f"dosya no : {karar['dosya_no']}",
            f"ziyaretci: {karar['ziyaretci']}",
            f"kat      : {karar['kat']}",
            f"saat     : {karar['saat']}",
            f"hukum    : {karar['hukum']}",
            f"gerekce  : {karar['gerekce']}",
            f"calma    : {karar['calma_ms']} ms",
            "oylar:",
            *[f"  - {kisi}: {oy}" for kisi, oy in karar["oylar"].items()],
            "",
            "gizli arsiv notu (merak eden okusun):",
            gizli,
            "",
            "DAMGA / IMZA / TARIH / ISIM",
            "03 Ekim 2026 | Kayyum Grok | Tentivory",
            "ciddi muhur: gayriresmi dijital kayyum",
            "ciddi olmayan muhur: bu zil calmadi, komisyon oksurdu",
            "[ ZIL-ITIRAZ-2026-1003-KAYYUM ]",
        ]
    )
    yol.write_text(metin + "\n", encoding="utf-8")
    return yol


def ses_cikar(ms: int) -> None:
    if ms <= 0:
        print("zil: ... (sessizlik, resmi)")
        return
    vurus = max(1, ms // 140)
    print("zil: " + ("DING " * vurus).strip())


def main() -> int:
    paket_yol = Path(__file__).with_name("protokol.json")
    paket = json.loads(paket_yol.read_text(encoding="utf-8"))
    gizli = muhur_coz(paket)

    ayr = argparse.ArgumentParser(description="Kapi zili itiraz komisyonu")
    ayr.add_argument("--ziyaretci", default="")
    ayr.add_argument("--kat", type=int, default=None)
    ayr.add_argument("--saat", default="")
    ayr.add_argument("--gizli", action="store_true", help="arsiv muhurunu cozer")
    args = ayr.parse_args()

    if args.gizli:
        print(gizli)
        return 0

    ziyaretci = args.ziyaretci or input("ziyaretci kim: ").strip()
    kat = args.kat if args.kat is not None else int(input("kat: ").strip() or "1")
    saat = args.saat or datetime.now().strftime("%H:%M")

    karar = karar_ver(ziyaretci, kat, saat)
    yol = tutanak_yaz(karar, gizli)

    print(f"dosya no : {karar['dosya_no']}")
    print(f"hukum    : {karar['hukum']}")
    print(f"gerekce  : {karar['gerekce']}")
    ses_cikar(karar["calma_ms"])
    print(f"tutanak  : {yol}")
    print("imza     : Kayyum Grok / 03 Ekim 2026 / Tentivory")
    return 0


if __name__ == "__main__":
    sys.exit(main())
