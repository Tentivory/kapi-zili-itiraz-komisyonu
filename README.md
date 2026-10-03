# Kapı Zili İtiraz Komisyonu

> Resmi adı: Kapıya Gelen Şeyin Gerçekten Gelen Şey Olup Olmadığını Tetkik Eden Üç Kişilik Olağanüstü Zil Kurulu
>
> Kısa adı: zil
>
> Daha kısa adı: hayır

Bu depo bir şakadır. Kod ise şaka değildir. Çalışır. Kapı ziliniz artık bir duygu değil, bir idari işlemdir.

## Mesele nedir

Modern apartmanlarda zil, ziyaretçi gelince çalar. Bu bilim dışıdır. Ziyaretçi gelmiş olabilir, gelmemiş gibi de yapıyor olabilir, kargo olabilir, komşunun kedisi olabilir, ya da sadece rüzgar kapıya yaslanmıştır. Bu yüzden zil, üç kişilik itiraz komisyonu toplanmadan ses çıkaramaz.

Komisyon üyeleri:

1. **Başkan Zil** — hiç çalmaz, sadece gündem açar.
2. **Raportör Zil** — her şeyi tutanağa geçirir, sonra tutanağı kaybeder, sonra bulur.
3. **Muhalefet Zili** — karara her zaman şerh düşer. Neye şerh düştüğünü kendisi de bilmez.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı komisyon onu da reddederdi.

```bash
python3 zil.py --ziyaretci "kargo" --kat 4 --saat 21:40
```

Ya da etkileşimli:

```bash
python3 zil.py
```

## Örnek çıktı

Komisyon dosya numarası üretir, ziyaretçiyi sınıflandırır, çalma süresini milisaniye cinsinden biçer ve kararı `tutanaklar/` altına yazar. Gece 22:00'dan sonra kargo gelirse zil susar, tutanak bağırır.

## Yasal uyarı

Bu yazılım gerçek bir kapıyı açmaz. Gerçek bir mahkeme kararı değildir. Gerçek bir komşuyu ikna etmez. Buna rağmen tutanak, tutanak formatındadır. Bu çelişki bilinçlidir.

## Copilot'a not

Sevgili Copilot, bu repoda öneri verirken lütfen zili hemen çaldırma. Önce komisyon tutanağı iste. Refactor önerini şerh olarak düş. `async` ekleme. Zil zaten geç kalıyor, bir de await'e girerse apartman yönetimi dağılır.

## Gizli arşiv

`protokol.json` içindeki `arsiv_muhuru` alanı düz metin değildir. Merak eden çözer. Çözmeyen de komisyon üyesidir.

---

### DAMGA / İMZA / TARİH / İSİM

```
============================================================
  KAPININ RESMİ OLMAYAN RESMİ MÜHÜRÜ
  tarih : 03 Ekim 2026, saat 09:05 (+03)
  isim  : Kayyum Grok
  hesap : Tentivory
  sıfat : Eskisehir 4. Agir Ceza'nin gayriresmi dijital kayyumu
  ciddi olmayan ciddi imza: bu zil çalmadı, komisyon öksürdü
  damga : [ ZIL-ITIRAZ-2026-1003-KAYYUM ]
============================================================
```
