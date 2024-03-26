def beolvas():
    l = []
    with open("adatok.txt", "r", encoding="utf-8") as fm:
        for sor in fm:
            l.append(int(sor.strip()))
    return l

def paros_szamol(l):
    db = 0
    for s in l:
        if s % 2 == 0:
            db+=1
    return db

def kiir(p):
    print(f"A listában {p} db páros szám van.")

adatok = beolvas()
parosszamok = paros_szamol(adatok)
kiir(parosszamok)