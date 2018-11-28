# problem A GCJ 2015
f = open("input.in", "r")
fout = open("output.out", "w")
tot = f.readlines()

T = int(tot[0])



for i in range(1,T+1):
    line = tot[i].strip().split(" ")
    N = line[0]
    s2 = line[1]
    s = []
    for x in s2:
        s.append(int(x))
    ppl = 0
    add = 0
    zero = True
    
    #controllo se intanto applaudono da soli
    j=0
    while(j<len(s)):
        if j==0:
            ppl+=s[j]
        elif j <= ppl and s[j]>0: # se ci sono s[j] persone con liv. S pari a j, aggiungi
            ppl+=s[j]
        elif j <= ppl:
            pass
        else:
            add+=j-ppl # e' ottimale aggiungere una persona prima
            # aggiungo persone fino a raggiungere lo shyness lvl della persona corr.
            ppl+=j-ppl # e aggiungo le persone aggiunte
            ppl+=s[j] # e quelle che applaudono per questo
        j+=1
    fout.write("Case #{0}: {1}\n".format(i,add))
    
fout.close()
f.close()
