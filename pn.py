import phonenumbers
import sys

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def banner():
	print("""
 ██▀███   ▄▄▄       ██▓ ██ ▄█▀▄▄▄        ▄████ ▓█████
▓██ ▒ ██▒▒████▄    ▓██▒ ██▄█▒▒████▄     ██▒ ▀█▒▓█   ▀
▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒▓███▄░▒██  ▀█▄  ▒██░▄▄▄░▒███
▒██▀▀█▄  ░██▄▄▄▄██ ░██░▓██ █▄░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄
░██▓ ▒██▒ ▓█   ▓██▒░██░▒██▒ █▄▓█   ▓██▒░▒▓███▀▒░▒████▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓  ▒ ▒▒ ▓▒▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░
  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░░ ░▒ ▒░ ▒   ▒▒ ░  ░   ░  ░ ░  ░
  ░░   ░   ░   ▒    ▒ ░░ ░░ ░  ░   ▒   ░ ░   ░    ░
   ░           ░  ░ ░  ░  ░        ░  ░      ░    ░  ░
Black Eye Community | https://github.com/rohmadhidayah""")
banner()

try:
	text = input("\033[1;41mTips: masukkan nomor dengan kode negara kamu (+62)\033[0m\n\033[1;36m[*] Masukkan nomor: \033[0m")
	if text == "":
		print("\033[1;41mMasukin nomor!\033[0m")
		sys.exit()

	pn = phonenumbers.parse(text)
	x = geocoder.description_for_number(pn,"en")
	y = carrier.name_for_number(pn,"en")
	z = timezone.time_zones_for_number(pn)

	print("\033[1;33m> \033[1;32mInfo\033[0m: ",pn)
	print("\033[1;33m> \033[1;32mDapat dihubungi secara internasional\033[0m: ",phonenumbers.can_be_internationally_dialled(pn))
	print("\033[1;33m> \033[1;32mBiaya\033[0m: ",phonenumbers.expected_cost(pn))
	print("\033[1;33m> \033[1;32mBersifat spesifik\033[0m: ",phonenumbers.is_carrier_specific(pn))
	print("\033[1;33m> \033[1;32mNomor geografis\033[0m: ",phonenumbers.is_number_geographical(pn))
	print("\033[1;33m> \033[1;32mNomor yang mungkin\033[0m: ",phonenumbers.is_possible_number(pn))
	print("\033[1;33m> \033[1;32mNomor-nya beralasan\033[0m: ",phonenumbers.is_possible_number_with_reason(pn))
	print("\033[1;33m> \033[1;32mNomor-nya pendek\033[0m: ",phonenumbers.is_possible_short_number(pn))
	print("\033[1;33m> \033[1;32mNomor-nya valid\033[0m: ",phonenumbers.is_valid_number(pn))
	print("\033[1;33m> \033[1;32mNomor pendek-nya valid\033[0m: ",phonenumbers.is_valid_short_number(pn))
	print("\033[1;33m> \033[1;32mPanjang kode wilayah geografis\033[0m: ",phonenumbers.length_of_geographical_area_code(pn))
	print("\033[1;33m> \033[1;32mPanjang kode tujuan nasional\033[0m: ",phonenumbers.length_of_national_destination_code(pn))
	print("\033[1;33m> \033[1;32mNomor nasional\033[0m: ",phonenumbers.national_significant_number(pn))
	print("\033[1;33m> \033[1;32mNomor internasional\033[0m: ",phonenumbers.normalize_digits_only(pn))
	print("\033[1;33m> \033[1;32mISP\033[0m: ",y)
	print("\033[1;33m> \033[1;32mTime zone\033[0m: ",z)
	print("\033[1;33m> \033[1;32mTipe nomor\033[0m: ",phonenumbers.number_type(pn))
	print("\033[1;33m> \033[1;32mLokasi\033[0m: ",x)
	print("\033[1;33m> \033[1;32mSingkatan\033[0m: ",phonenumbers.region_code_for_number(pn))
	print("\033[1;33m> \033[1;32mNomor terlalu panjang\033[0m: ",phonenumbers.truncate_too_long_number(pn))

except KeyboardInterrupt:
	print("\033[1;41mThanks for use!\033[0m")
