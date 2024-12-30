import sys
import re
import json
from datetime import datetime


hacks_str=""
if(len(sys.argv) > 1):
    hacks_str=sys.argv[1]
dataset={}

with open('dataset.json') as f:
    dataset = json.load(f)

for id_str in hacks_str.split(";"):
    if(id_str!=""):
        id_num=int(id_str)
        try:
            for hack in dataset["hacks"]:
                if(hack["id"]==id_num):
                    print("Apply hack"+hack["name"])
                    data=""
                    with open(hack["file"], 'r') as file: 
                        data=file.read()
                        data = data.replace(hack["search"], hack["replace"])
                    with open(hack["file"], 'w') as file:
                        file.write(data)
        except Exception:
            print("cannot apply hack with id="+id_str)
            pass

try:
    with open("wled00/data/settings_sec.htm", 'r') as file:
        data=file.read()
        data = data.replace("##VERSION##", '##VERSION##<br>Compiled using <a href="https://wled-compile.github.io/" target="_blank">online wled compiler</a> provided by <a href="https://shop.myhome-control.de" target="_blank">MyHome-Control</a><br>(compile UTC date/time: '+datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')+')')
    with open("wled00/data/settings_sec.htm", 'w') as file:
        file.write(data)
except Exception:
    print("cannot add version info")
    pass
