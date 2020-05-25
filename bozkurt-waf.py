#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("pkg install figlet -y")
os.system("pkg install nmap -y")
os.system("clear")
os.system("figlet WAF")
print("""
Bu araç nmap kullanarak hedef sistemde güvenlik duvarı olup olmadığını kontrol eder. Varsa güvenlik duvarının ne olduğu tespit etmeye çalışır.
			Bozkurt Noyan
""")

hedef = input("Hedef : ")
os.system("nmap " + hedef + " -p 80 --script http-waf-detect,http-waf-fingerprint")
