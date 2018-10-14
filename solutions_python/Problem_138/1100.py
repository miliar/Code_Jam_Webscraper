def dwar(NAOMI , KEN):
    naomi = NAOMI[:]
    ken = KEN[:]
    naomi.sort()
    ken.sort()
    a=len(naomi)
    ans=0
    for i in range(a):
        if naomi[0]>ken[0]:
            naomi=naomi[1:]
            ken=ken[1:]
            ans+=1
        else:
            naomi=naomi[1:]
            
            ken=ken[:-1]
            
    return ans
    

def war(NAOMI,KEN):
    naomi = NAOMI[:]
    ken = KEN[:]
    naomi.sort()
    ken.sort()
    a=len(naomi)
    ans=0
    for i in range(a):
        if naomi[-1]>ken[-1]:
            naomi=naomi[:-1]
            ken=ken[1:]
            ans+=1
            
        else:
            naomi=naomi[:-1]
            ken=ken[:-1]
    return ans


f = open('D-large.in', 'r')
line1 = f.readline()
cases = int(line1)
for case in range(1,cases+1):
    line = f.readline()
    N = int(line)
    line = f.readline()
    naomi_str = line.split()
    naomi = [float(naomi_str[i]) for i in range(N)]
    line = f.readline()
    ken_str = line.split()
    ken = [float(ken_str[i]) for i in range(N)]

    print "Case #"+str(case)+ ": " + str(dwar(naomi,ken)) + " " + str(war(naomi,ken))
