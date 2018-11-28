def war(naomi, ken):
    naomic = naomi.copy()
    kenc = ken.copy()
    naomic.sort()
    kenc.sort()
    for i in range(len(naomic)):
        if naomic[i]>max(kenc):
            return len(naomic)-i
        index=0
        while kenc[index]<naomic[i]:
            index+=1
        kenc.pop(index)
    return 0

def deceitfulWar(naomi, ken):
    naomic = naomi.copy()
    kenc = ken.copy()
    naomic.sort()
    kenc.sort()
    points=0
    for i in range(len(naomic)):
        if naomic[i]<min(kenc):
            kenc.pop()
        else:
            kenc.pop(0)
            points+=1
    return points

fin = open('D-large.in')
fout = open('output.out', 'w')

lineNb=0
for line in fin:
    if lineNb==0:
        lineNb+=1
        continue
    if lineNb%3==1:
        naomi=[]
        ken=[]
    if lineNb%3==2:
        numbers = line.strip().split(" ")
        for n in numbers:
            naomi.append(float(n))
    if lineNb%3==0:
        numbers = line.strip().split(" ")
        for n in numbers:
            ken.append(float(n))
        fout.write("Case #"+str(lineNb//3)+": "+str(deceitfulWar(naomi, ken)))
        fout.write(" "+str(war(naomi, ken))+"\n")
    lineNb+=1
    
fout.close()
