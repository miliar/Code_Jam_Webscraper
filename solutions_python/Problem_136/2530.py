#!/usr/bin/python

def calcola(c, f, x):
    ipotesi_precedente = -1
    prod_sec = 2
    finito = False
    secondi_totali = 0.
    count = 0

    while not finito:
        count += 1
        secondi_farm = c / prod_sec
        secondi_cookies = x / prod_sec

        ipotesi_corrente = secondi_totali + secondi_cookies
        if ipotesi_precedente == -1 or ipotesi_precedente > ipotesi_corrente:
            ipotesi_precedente = ipotesi_corrente
            secondi_totali += secondi_farm
            prod_sec += f
        else:
            finito = True
            secondi_totali += secondi_cookies
            return ipotesi_precedente

out_file = open("B-large.out","w+")

fname = "B-large.in"
with open(fname) as f:
    content = f.readlines()
    
i = 0
for line in content:
    if i > 0:
        ll = line.rstrip("\n").split(" ")
        out_file.write("Case #%d: %.7f\n" % (i, calcola (float(ll[0]),float(ll[1]),float(ll[2]))))

    i += 1

out_file.close()
