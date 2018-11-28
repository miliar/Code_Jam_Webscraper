f = open("A-small-attempt0.in", "r")
fout = 'out'
out = open(fout, 'w')

case = f.readline()
num = int(case)
debout = 0
indice = 0
res = 0
tot = 0
for i in range(1,num +1):
    line = f.readline()
    liste = line.split(" ")
    indice = int(liste[0])
    liste2 = liste[1].split("\n")
    debout = 0
    res = 0
    tot=0
    indice = 0
    for j in liste2[0]:
        if ((debout < indice) & (int(j) != 0)):
            res += indice - debout
            debout += res
        debout += int(j)
        indice += 1
        #tot += int(j)
    print('Case #'+ str(i)+ ': '+ str(res))
    out.write('Case #'+ str(i)+ ': '+ str(res) + '\n')
f.close()
