out = open("Output.txt", "w")

def tell_time(x,f):#Functie ce ne spune in cat timp ajungem la tinta x
    return x/f
i = 0
for e in open("Input.txt", "r"):
    if i != 0:
        cookies_pe_secunda = 2#Atatea primesc initial pe secunda
        e = e.split()
        c = float(e[0])#Costul unei ferme
        f = float(e[1])#Productia unei ferme pe secunda
        x = float(e[2])#My cookie quantity target!
        One_Case = tell_time(x,cookies_pe_secunda)
        timp_minim = -1
        inainte = timp_minim_now = 0
        while True:
            timp_o_ferma = tell_time(c, cookies_pe_secunda)
            inainte += timp_o_ferma
            cookies_pe_secunda += f
            timp_minim_now = inainte + tell_time(x, cookies_pe_secunda)
            if timp_minim < 0:#Initializarea timpului minim, only once executes
                timp_minim = timp_minim_now
            if timp_minim < timp_minim_now:
                break
            timp_minim = timp_minim_now
        if timp_minim > One_Case:
            timp_minim = One_Case
        out.write("Case #" +str(i)+ ": " + str(timp_minim) + "\n")
    i += 1
out.close()
