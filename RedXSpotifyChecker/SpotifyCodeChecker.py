import os
import time
import datetime

print("Gerekli Modüller İndirilip Derleniyor...")


try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except ImportError:
    os.system("pip install selenium")

try:
    from colorama import Fore, init
except ImportError:
    os.system("pip install colorama")

init(autoreset=True)
os.system("cls")
print(Fore.GREEN + "Başarılı! Developer by " + Fore.RED + "FuryLemons")

print(Fore.RED + '''
██████╗░ ███████╗ ██████╗░ ██╗░░██╗
██╔══██╗ ██╔════╝ ██╔══██╗ ╚██╗██╔╝
██████╔╝ █████╗░░ ██║░░██║ ░╚███╔╝░
██╔══██╗ ██╔══╝░░ ██║░░██║ ░██╔██╗░
██║░░██║ ███████╗ ██████╔╝ ██╔╝╚██╗
╚═╝░░╚═╝ ╚══════╝ ╚═════╝░ ╚═╝░░╚═╝''')

time.sleep(2)

os.system("cls")

def main():
    print("Tarayıcı Başlatılıyor.") 
    time.sleep(1)
    os.system("cls")

    print(Fore.LIGHTGREEN_EX + "Tarayıcı Başlatılıyor..")
    time.sleep(1)
    os.system("cls")

    print(Fore.GREEN + "Tarayıcı Başlatılıyor...")
    time.sleep(1)
    os.system("cls")

    try:
        driver = webdriver.Chrome()
        driver.get("https://accounts.spotify.com/tr/login")
    except Exception:
        print(Fore.RED + "Tarayıcı başlatılamadı!" )
        exit()

    time.sleep(3)

    print(Fore.GREEN + "Başarılı! Tarayıcı Başlatıldı.")

    time.sleep(1)
    os.system("cls")

    print(Fore.GREEN + "Spotify'a giriş yapıldı.")

    time.sleep(1)
    os.system("cls")

    email = "mail gir"
    password = "sifre gir"

    email_input = driver.find_element(By.ID, "login-username")
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, "login-password")
    password_input.send_keys(password)

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(3)

    if "Login - Spotify" in driver.title or "Oturum aç - Spotify" in driver.title:
        print(Fore.RED + "Giriş Başarısız: Kullanıcı adı veya parola yanlış.")
        time.sleep(2)
        driver.quit()  
        exit()
    else:
        print(Fore.GREEN + "Giriş Başarılı")

    time.sleep(3)
    os.system("cls")

    input_file = input("Dosya adını giriniz [örn:codes.txt]: ")

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f"results_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    output_file_good = os.path.join(output_dir, "good.txt")
    output_file_invalid = os.path.join(output_dir, "invalid_bad.txt")
    output_file_remaining = os.path.join(output_dir, "remaining.txt")

    time.sleep(1)
    os.system("cls")

    try:
        with open(input_file, "r") as file:
            codes = file.readlines()
    except Exception:
        print(Fore.RED + input_file + " Bulunamadı!")
        exit()

    print(Fore.GREEN + input_file + " Bulundu!")

    time.sleep(1)
    os.system("cls")

    print(Fore.BLACK + "İşlem Başlatılıyor.")
    os.system("cls")
    print(Fore.BLACK + "İşlem Başlatılıyor..")
    os.system("cls")
    print(Fore.BLACK + "İşlem Başlatılıyor..")
    os.system("cls")

    with open(output_file_good, "w") as valid_codes, \
        open(output_file_invalid, "w") as invalid_codes, \
        open(output_file_remaining, "w") as remaining_codes:

        for code in codes:
            code = code.strip()
            
            driver.get("https://www.spotify.com/tr-en/ppt/hm/redeem/")
            code_input = driver.find_element(By.NAME, "code")
            code_input.send_keys(code)
            
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            
            time.sleep(3)
                
            if driver.current_url != "https://www.spotify.com/tr-en/ppt/hm/redeem/":
                valid_codes.write(code + "\n")
                print(f"{Fore.GREEN}[+] Kod geçerli: {code}")
            elif "The code you entered is invalid" in driver.page_source:
                invalid_codes.write(code + "\n")
                print(f"{Fore.RED}[-] Kod geçersiz: {code}" )
            elif "Unfortunately this Premium code does not seem to be valid. Try again or contact customer service." in driver.page_source:
                invalid_codes.write(code + "\n")
                print(f"{Fore.RED}[-] Kod geçersiz: {code}")
            else:
                remaining_codes.write(code + "\n")
                print(f"{Fore.RED}[?] Bu kodla ilgili bilinmeyen bir durum var: {code}")
    
    os.system("cls")

    print(Fore.GREEN + "İşlemler tamamlandı.\n")
    print(Fore.GREEN + f"Sonuçlar {output_dir} dizininde bulunuyor.")
    time.sleep(2)

    driver.quit()

main()

os.system("cls")

print(Fore.RED + '''
██████╗░ ███████╗ ██████╗░ ██╗░░██╗
██╔══██╗ ██╔════╝ ██╔══██╗ ╚██╗██╔╝
██████╔╝ █████╗░░ ██║░░██║ ░╚███╔╝░
██╔══██╗ ██╔══╝░░ ██║░░██║ ░██╔██╗░
██║░░██║ ███████╗ ██████╔╝ ██╔╝╚██╗
╚═╝░░╚═╝ ╚══════╝ ╚═════╝░ ╚═╝░░╚═╝''')

secim = int(input(f"\n1 => {Fore.CYAN}Başka bir dosya ile devam et\n{Fore.RESET}2 => {Fore.RED}Çıkış\n\n{Fore.RESET}"))

if secim == 1:
    main()
elif secim == 2:
    exit()
else:
    print(Fore.RED + "| -- ERROR -- |")
    time.sleep(1)
    exit()