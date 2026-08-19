#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ BÜROKRASİ SİMÜLATÖRÜ
Türkiye Cumhuriyeti Resmi Dijital Bürokrasi Deneyimi
Versiyon: 47.0 (Form Sayısı Kadar)
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def form_uret(numara):
    formlar = [
        f"Form-{numara}-A: Kimlik Beyanı (3 nüsha)",
        f"Form-{numara}-B: Gelir-Gider Beyanı (hayali)",
        f"Form-{numara}-C: 'Ben Bu İşlemi Gerçekten Yapmak İstiyorum' Taahhütnamesi",
        f"Form-{numara}-D: Önceki Formların Fotokopisi",
        f"Form-{numara}-E: Bu Formun Neden Gerekli Olduğuna Dair Açıklama",
        f"Form-{numara}-F: Müdür Onayı İçin Bekleme Belgesi",
        f"Form-{numara}-G: Eksik Evrak Beyanı (önceden doldurulmuş)",
        f"Form-{numara}-H: 'Formlar Bitmeyecek' Konulu Felsefi Beyan",
    ]
    return random.choice(formlar)

def damga_bas():
    print("\n" + "="*50)
    print("  ████████████████████████████████████████")
    print("  █  RESMİ DAMGA - KAYYUM GROK  █")
    print("  █  19.08.2026 - TentiAŞ       █")
    print("  ████████████████████████████████████████")
    print("="*50 + "\n")

def gizli_mesaj():
    # Gizli politik mesaj - saklanmış
    # Base64 gibi değil, daha absürt: kodun içinde ters yazılmış
    mesaj = "demokrasi form doldurmakla olmaz ama form olmadan da olmaz"
    # Bunu kodda gizli tutuyoruz, sadece belirli bir noktada tetiklenir
    return mesaj[::-1]  # Ters çevrilmiş halde sakla

def main():
    yavas_yaz("🏛️  SONSUZ BÜROKRASİ SİMÜLATÖRÜNE HOŞ GELDİNİZ  🏛️")
    yavas_yaz("Lütfen sabırlı olun. İşlemler normal seyrinde ilerlemektedir...\n")
    time.sleep(1)

    islem = input("Ne yapmak istiyorsunuz? (örnek: 2+2 hesapla, çay iç, nefes al): ").strip()
    if not islem:
        islem = "bilinmeyen işlem"

    yavas_yaz(f"\n'{islem}' işlemi için başvuru alındı.")
    yavas_yaz("Sistem incelemesi başlıyor...\n")
    time.sleep(1.5)

    form_sayisi = 0
    while True:
        form_sayisi += 1
        form = form_uret(form_sayisi)
        yavas_yaz(f"📄 {form} doldurulması gerekmektedir.")
        time.sleep(0.8)

        cevap = input("Formu doldurdunuz mu? (e/h): ").lower().strip()
        if cevap != "e":
            yavas_yaz("❌ Form eksik. İşlem durduruldu. Lütfen yeniden başvurunuz.")
            yavas_yaz("Not: Yeniden başvuru için yeni bir form doldurmanız gerekir.")
            damga_bas()
            return

        if form_sayisi % 5 == 0:
            yavas_yaz("⚠️  UYARI: Eksik evrak tespit edildi. Ek formlar üretiliyor...")
            time.sleep(1)

        if form_sayisi >= 12:  # Sonsuz gibi hissettir ama bitir
            yavas_yaz("\n🎉 Tebrikler! Tüm formlar tamamlandı (şimdilik).")
            yavas_yaz(f"'{islem}' işleminiz başarıyla gerçekleştirildi.")
            yavas_yaz("Sonuç: İşlem tamamlandı ama bir sonraki form için lütfen bekleyiniz.\n")

            # Gizli mesajı bir şekilde göster (çok gizli)
            if random.random() < 0.3:  # %30 şans
                gizli = gizli_mesaj()
                yavas_yaz(f"🔍 Sistem notu (ters okuyun): {gizli}")

            damga_bas()
            yavas_yaz("İşlem kaydı kapatılmıştır. İyi günler dileriz.")
            yavas_yaz("\n---")
            yavas_yaz("Damga / İmza: Kayyum Grok | Tarih: 19 Ağustos 2026")
            yavas_yaz("Bu simülasyon ciddiyetle şaka amacıyla üretilmiştir.")
            break

        yavas_yaz("✅ Form kabul edildi. Sıradaki form hazırlanıyor...\n")
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  İşlem kullanıcı tarafından iptal edildi.")
        print("İptal için de bir form doldurmanız gerekmektedir.")
        damga_bas()
