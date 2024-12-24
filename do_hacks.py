import sys
import re
import json


hacks_str=sys.argv[1]
dataset={}

with open('dataset.json') as f:
    dataset = json.load(f)

for id_str in hacks_str.split(";"):
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