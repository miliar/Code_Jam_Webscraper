def dwar(NAOMI , KEN):
    naomi = NAOMI[:]
    ken = KEN[:]
    naomi.sort()
    ken.sort()
    N = len(naomi)
    count = 0
    for turn in range(N):
        if naomi[0] > ken[0]:
            count += 1
            naomi = naomi[1:]
            ken = ken[1:]
        else:
            naomi = naomi[1:]
            ken = ken[:-1]
    return count

def war(NAOMI ,KEN):
    naomi = NAOMI[:]
    ken = KEN[:]
    naomi.sort()
    ken.sort()
    N = len(naomi)
    count = 0
    for turn in range(N):
        if naomi[-1] > ken[-1]:
            count += 1
            naomi = naomi[:-1]
            ken = ken[1:]
        else:
            naomi = naomi[:-1]
            ken = ken[:-1]
    return count
    

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
