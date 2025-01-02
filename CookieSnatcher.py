import requests
import http.cookiejar as cookiejar
from colorama import Fore, init

init(autoreset=True)

cookie_jar = cookiejar.CookieJar()

session = requests.Session()
session.cookies = cookie_jar

url = input(f"{Fore.GREEN}Veuillez entrer l'URL : ")

response = session.get(url)

print(f"{Fore.GREEN}Cookies récupérés :")
for cookie in cookie_jar:
    print(f"{Fore.GREEN}Nom: {cookie.name}, Valeur: {cookie.value}")

input(f"{Fore.YELLOW}Appuyez sur Entrée pour fermer...")