# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 08:41:08 2023

@author: tolga-ertugrul
"""
import re

def check_password(password):
    #Şifre uzunluğu 4 ile 8 arasında olabilir:
    if len(password) < 4:
        return "Geçersiz Şifre \nŞifre çok kısa"
    elif len(password) >8:
        return "Geçersiz Şifre \nŞifre en fazla 8 karakter olabilir"

    #İngiliz alfabesindeki küçük harflerden en az bir adet yer almalıdır:
    if not re.search("[a-z]", password):
        return "Geçersiz Şifre \nŞifre en az bir küçük harf içermeli"
    
    #İngiliz alfabesindeki büyük harflerden en az bir adet yer almalıdır.
    if not re.search("[A-Z]", password):
        return "Geçersiz Şifre \nŞifre en az bir büyük harf içermeli"
    
    #En az bir rakam bulunmalıdır
    if not re.search("[0-9]", password):
        return "Geçersiz Şifre \nŞifre en az bir rakam içermeli"
    
    #Karakterlerden en az biri şifrede yer almalıdır
    allowed_special_characters = set(['(', ')', '*', '+', ',', '-', '.'])
    if not all(char.isalnum() or char in allowed_special_characters for char in password):
        return "Geçersiz Şifre \nŞifre izin verilen özel karakterlerden en az birini içermeli"
    
    #Koşullar sağlandığında skor hesapla   
    lowercase_count = sum(1 for char in password if char.islower())
    uppercase_count = sum(1 for char in password if char.isupper())
    digit_count = sum(1 for char in password if char.isdigit())
    special_char_count = sum(1 for char in password if not char.isalnum())

    score = 3 * (lowercase_count + 1) * 5 * (uppercase_count + 1) * 2 * (digit_count + 1) * 4 * (special_char_count + 1) - 120

    # Skora göre durum
    if score < 2000:
        return "Geçerli Şifre \nÇok Zayıf Şifre"
    elif 2000 <= score < 4000:
        return "Geçerli Şifre \nZayıf Şifre"
    elif 4000 <= score < 6000:
        return "Geçerli Şifre \nOrtalama Şifre"
    elif 6000 <= score < 9000:
        return "Geçerli Şifre \nGüçlü Şifre"
    else:
        return "Geçerli Şifre \nÇok Güçlü Şifre"

# Kullanıcıdan şifreyi al
user_password = input("Lütfen bir şifre girin: ")

# Şifre kontrolü yap ve sonucu ekrana bas
result = check_password(user_password)

print(result)