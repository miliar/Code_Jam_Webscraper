from math import ceil, floor, sqrt

def pals(lower):
    size = len(str(lower))
    halfpal = 0
    if size % 2 == 0:
        halfpal = int(str(lower)[:len(str(lower))/2])
        if int(str(halfpal)+str(halfpal)[::-1]) < lower:
            halfpal = int(str(lower)[:len(str(lower))/2])+1
    else:
        halfpal = int(str(lower)[:(len(str(lower))+1)/2])
        if int(str(halfpal)+str(halfpal)[::-1][1:]) < lower:
            halfpal = int(str(lower)[:(len(str(lower))+1)/2])+1
    while True:
        if size % 2 == 0:
            yield int(str(halfpal)+str(halfpal)[::-1])
        else:
            yield int(str(halfpal)+str(halfpal)[::-1][1:])

        if len(set(str(halfpal))) <= 1 and halfpal%10 == 9:
            if size % 2 == 0:
                halfpal += 1
            else:
                halfpal += 1
                halfpal = halfpal / 10
            size += 1
        else:
            halfpal += 1
    
def ispal(n):
    return str(n) == str(n)[::-1]

fin = open("C-large-1.in", "r")
fout = open("fdsa.txt", "w")
T = int(fin.readline())
for i in range(T):
    a,b = fin.readline().split()
    a = int(a)
    b = int(b)
    tot = 0
    #print a,b
    for pal in pals(int(ceil(sqrt(a)))):
        if pal**2 > b:
            break
        if ispal(pal**2):
           tot += 1 
    #print tot
    fout.write("Case #"+str(i+1)+": "+str(tot)+"\n")
    
fin.close()
fout.close()
