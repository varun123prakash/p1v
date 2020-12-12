import random
club={"Arsenal":"ENG","Astana":"KAZ", "Atlético": "ESP", "Barcelona" :"ESP","BATE": "BLR",
    "Bayern":"GER","Benfica": "POR","Chelsea":"ENG","CSKA Moskva" :"RUS","Dinamo Zagreb" :"CRO",
"Dynamo Kyiv" :"UKR","Galatasaray": "TUR","Gent":"BEL","Juventus": "ITA","Leverkusen": "GER",
"Lyon": "FRA","M. Tel-Aviv":"ISR","Malmö":"SWE","Man. City":"ENG","Man. United":"ENG",
"Mönchengladbach":"GER","Olympiacos":"GRE","Paris": "FRA","Porto":"POR","PSV": "NED",
"Real Madrid": "ESP","Roma": "ITA","Sevilla": "ESP","Shakhtar Donetsk" :"UKR","Valencia":"ESP",
"Wolfsburg" :"GER" ,"Zenit":"RUS"}
k=list(club.items())
random.shuffle(k)
club=dict(k)
c=0
l=[]
ch=65
print("Group A")
for x,y in club.items():
    if y in l:
        club[x]=y
        continue
    else:
        l.append(y)
        print(x)
        c+=1
        if c==4:
            l.clear()
            ch+=1
            if ch!=73:
                print("\r")
                print("Group",chr(ch))
            c=0