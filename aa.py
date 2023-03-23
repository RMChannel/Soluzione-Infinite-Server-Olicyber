import requests
import os
game=True
r=requests.get("http://infinite.challs.olicyber.it/")
i4=0
while game:
    i4+=1
    result=0
    cookie=r.cookies
    color=False
    body=(r.text)
    if "GRAMMAR TEST" in body:
        for i in body.split("\n"):
            if "Quant" in i:
                line=i
        key1=False
        for i in line:
            if key1:
                letter=i
                break
            elif i=='"': key1=True
        print(letter)
        istring=0
        string=""
        for i in line:
            if istring==3:
                string+=i
            if i=='"': istring+=1
        string=string[:-1]
        print(string)
        for i in string:
            if letter==i:
                result+=1
        print(result)
    elif "MATH TEST" in body:
        for i in body.split("\n"):
            if "Quant" in i:
                line=i
        line=line.replace("<p>Quanto fa ","")
        line=line.replace("?</p>","")
        line=line.replace(" ","")
        key1=False
        n1=""
        n2=""
        for i in line:
            if (i=='+'):
                key1=True
            elif not(key1):
                n1+=i
            else:
                n2+=i
        n1=int(n1)
        n2=int(n2)
        result=n1+n2
        print(n1,n2,result)
    elif "ART TEST" in body:
        for i in body.split("\n"):
            if "Premi" in i:
                line=i
        print(line)
        if "Rosso" in line:
            dati={"Rosso":""}
        elif "Verde" in line:
            dati={"Verde":""}
        else:
            dati={"Blu":""}
        color=True
    else:
        print(r.text)
        print(i4)
        os.system("pause")
    if not(color):
        dati={'letter':result,'submit':'Submit'}
    r=requests.post("http://infinite.challs.olicyber.it/", data=dati, cookies=cookie)
#LA RICHIESTA POST RICHIEDE letter COME RISULTATO E submit=Submit