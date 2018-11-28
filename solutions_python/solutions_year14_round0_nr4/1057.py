"""
Problem D
John S.
"""
import sys
inputfile = "D-large.in"
# inputfile = "D-small-attempt0.in"
# inputfile = "test.txt"
outputfile = "out.txt"
fi = open(inputfile)
g = open(outputfile, "w")
t = int(fi.readline().strip())

for pl in range(t):
    n = int(fi.readline().strip())
    naomi = [float(x) for x in fi.readline().split()]
    ken = [float(y) for y in fi.readline().split()]

    naomi.sort(reverse = True)
    ken.sort(reverse = True)
    #keep backup
    noriginal = list(naomi)
    koriginal = list(ken)
    #Regular war: 
    #Naomi plays first
    #If ken doesnt have a block to beat naomi,
    #he plays his smallest

    regularscore = 0
    while len(naomi)>0:
        nblock = naomi.pop(0)
        if nblock > max(ken):
            ken.pop(-1)
            regularscore+=1
        else:
            ken.pop(0)
    
    #deceitful war
    #Naomi plays first
    #Naomi can burn small blocks by bluffing
    #and remove ken's big blocks

    naomi = list(noriginal)
    ken = list(koriginal)

    otherscore = 0
    while len(naomi)>0:
        kblock = ken.pop(0)
        if kblock > max(naomi):
            naomi.pop(-1)
        else:
            otherscore+=1
            naomi.pop(0)

    m = pl + 1
    outstr = "Case #{0}: {1} {2}\n".format(m, otherscore, regularscore)
    sys.stdout.write(outstr)
    g.write(outstr)