def war(naomi,ken,n):
    for i in range(n):
        #print(naomi, ken)
        c1 = naomi[0]
        naomi = naomi[1:]
        for j in range(len(ken)):
            if ken[j] > c1:
         #       print(c1,ken[j],j)
                ken = ken[:j]+ken[j+1:]
                break
        else:
            return n-i
    return 0

def decWar(naomi,ken,n):
    wins = 0
    for i in range(n):
        c1 = ken[0]
        ken = ken[1:]
        for j in range(len(naomi)):
            if naomi[j] > c1:
                naomi = naomi[:j]+naomi[j+1:]
                break
        else:
            return i
    return n

f = open("D-large.in","r")
o = open("D-large-answers.txt","w")
T = int(f.readline())
for t in range(1,T+1):
    n = int(f.readline())
    naomi = [float(a) for a in f.readline().split()]
    ken = [float(a) for a in f.readline().split()]
    naomi.sort()
    ken.sort()
    sol = str(decWar(naomi,ken,n))+" "+str(war(naomi,ken,n))
    o.write("Case #"+str(t)+": "+sol+"\n")
o.close()
    
