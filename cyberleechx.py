#
#
# CYBERLEECH X
# By CYBER0PUNK
# https://www.nulled.to/user/2280672-cyber0punk
#
# Enjoy!
#
#

# Import packages
import pyfiglet
import requests
import re
import json
import random
from colorama import Fore, Back, Style, init

init()

# Define variables
foundType = False
pastebin_urls = []
combos = []

# Print intro
print(Fore.BLUE+pyfiglet.figlet_format("CYBERLEECH X"))
print(Fore.RED+'Made by CYBER0PUNK')
print('https://www.nulled.to/user/2280672-cyber0punk')
print(Fore.YELLOW+'Starting CYBERLEECH X...')
print()
print()

# Get combo type
while foundType == False :
    type = input(Fore.BLUE+'For User:Pass combos, type U, for Email:Pass type E: ')

    if (type.lower() == "u" or type.lower() == "e") == False:
        print(Fore.RED+'Please enter either U for User:Pass or E for Email:Pass!')
    else :
        foundType = True

type = type.upper()

keywords = ['emailpass+combos','email:pass+combos','email+combos','combolist','combos','combo+list','gaming+combo','streaming+combo','userpass+combo','shopping+combo','@gmail.com:','@yahoo.com:','@hotmail.com:','@protonmail.com:','@protonmail.ch:','mixed+combo','fresh+combo','minecraft+combo','fortnite+combo','new+combo','spotify+combo','spotify+hits','hulu+hits','netflix+hits','fortnite+hits','minecraft+hits','tidal+hits','spotify+accounts','netflix+accounts','fortnite+accounts','minecraft+accounts']

print(Fore.GREEN+'Starting leecher...')

for x in range(len(keywords)) :
    keyword = keywords[x]
    req = requests.get(url='https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=1000&hl=en&source=gcsc&gss=.com&cselibv=c96da2eab22f03d8&cx=013305635491195529773:0ufpuq-fpt0&q='+keyword+'&safe=off&cse_tok=AKaTTZhm0Hc0MewQXXRgueF9IV0a:1567525721124&sort=date&exp=csqr,4229469&callback=google.search.cse.api15354')
    regex = re.findall("https:\/\/pastebin.com\/[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]", req.text)
    for x in range(len(regex)) :
        pastebin_urls.append(regex[x])

pastebin_urls = list(dict.fromkeys(pastebin_urls))

print(Fore.GREEN+'Scraping URLS...')

for x in range(len(pastebin_urls)) :
    pastebin_url = pastebin_urls[x].replace('.com/','.com/raw/')
    print(Fore.BLUE+'Gathered URL: '+pastebin_url)
    req = requests.get(url=pastebin_url)
    regex = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:\w+",req.text)
    for x in range(len(regex)) :
        combos.append(regex[x])

combos = list(dict.fromkeys(combos))

file = 'combos-'+str(random.randint(1000000000,9999999999))+'.txt'
f = open(file,'a+')
for x in range(len(combos)) :
    combo = combos[x]
    if(type == "U") :
        combo = combo.split(':')
        email = combo[0]
        password = combo[1]
        combo = email.split('@')
        username = combo[0]
        combo = username+':'+password

    print(Fore.BLUE+combo)
    f.write(combo+'\n')
f.close()

print(Fore.YELLOW+'COMBO LEECHER X COMPLETED! Combos saved to '+Fore.RED+file)
print()
print(Fore.BLUE+pyfiglet.figlet_format("ENJOY!"))
