from selenium import webdriver
import requests,os,time,re
try:
    os.mkdir("çalınanlartxt")
except OSError:
    print("")
queryparameter = input("Anahtar Kelime : ")
print("Tarama İşlemi Başlatılıyor")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://www.google.com/search?q=" + queryparameter +"+site:throwbin.io&num=100")
links = []
for asd in chrome.find_elements_by_class_name("r"):
    links.append(asd.find_elements_by_css_selector("*")[0].get_attribute("href"))
    print(asd.find_elements_by_css_selector("*")[0].get_attribute("href"))
chrome.quit()
print(links)
kaçıncıindirkayder = 0
savedtimestamp = time.time()
print("Hesaplar Kaydediliyor")
os.mkdir("çalınanlartxt/" + str(savedtimestamp))
for link in links:
    reallink = ""
    if str(link).startswith("https://throwbin.io"):
        reallink = str(link)[20:]
        asd = requests.get("https://api.throwbin.io/v1/paste/"+ reallink + "/download/").text
        open("çalınanlartxt/"+str(savedtimestamp) + "/z" + str(kaçıncıindirkayder) + ".txt", 'a' , errors="ignore" , encoding="utf-8").write(str(asd))
        open("çalınanlartxt/"+str(savedtimestamp) + "/TOPLU.txt", 'a', errors="ignore" , encoding="utf-8").write(asd + "\n")
    else:
        dsa = requests.get(link).text
        open("çalınanlartxt/"+ str(savedtimestamp) + "/z" + str(kaçıncıindirkayder) + ".txt", 'a' , errors="ignore" , encoding="utf-8").write(str(dsa))
        open("çalınanlartxt/"+str(savedtimestamp) + "/TOPLU.txt", 'a', errors="ignore" , encoding="utf-8").write(dsa + "\n")
    print(str(kaçıncıindirkayder + 1) + "/" + str(len(links)))
    kaçıncıindirkayder += 1
print("Hesaplar Kaydedildi")
print("Hesaplar Ayıklanıyor")
croppeds = re.findall("\w{5,30}[@]?\w{1,10}[.]?\w{1,30}[:]\S+",open("çalınanlartxt/"+str(savedtimestamp) + "/TOPLU.txt", 'r', errors="ignore" , encoding="utf-8").read())
kaçıncıkırpıldı = 0
croppeds = list(dict.fromkeys(croppeds))
for cropped in croppeds:
    open("çalınanlartxt/" + str(savedtimestamp) + "/TEKTEK.txt", 'a', errors="ignore", encoding="utf-8").write(cropped + "\n")
    print(str(kaçıncıkırpıldı) + "/" + str(len(croppeds)))
    kaçıncıkırpıldı += 1
print("İşlem Tamam")
os.startfile(os.getcwd() + "\\çalınanlartxt\\" + str(savedtimestamp) + "\\TEKTEK.txt")



