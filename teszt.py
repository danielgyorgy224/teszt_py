def beolvas():
    l = []
    with open("adatok.txt", "r", encoding="utf-8") as fm:
        for sor in fm:
            l.append(int(sor.strip()))
    return l

def osszead(l):
    sum=0
    for szam in l:
        sum+=szam
    return sum

def kiir(s):
    print(s)

adatok = beolvas()
osszeg = osszead(adatok)
kiir(osszeg)