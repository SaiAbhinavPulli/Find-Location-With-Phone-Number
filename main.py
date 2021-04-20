import phonenumbers # pip install phonenumbers
from phonenumbers import geocoder
PhoneNumber = input("Enter your Phone number with the security code of your country")
ch_nmber = phonenumbers.parse(PhoneNumber, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))