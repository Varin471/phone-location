import phonenumbers as pn
from phonenumbers import geocoder

print("Exmaple: +66 XXX XXX XXXX")
input = str(input("Enter a phone number: "))
phone = pn.parse(input, None)
print(geocoder.description_for_number(phone, "en"))