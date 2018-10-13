import math

def cycTable(upper,dert):
    res = [1.0,0.0,2.0]
    for i in range(3,upper):
        addem = [dert[j]*res[j]/(math.factorial(j)*math.factorial(i-j)) for j in range(0,i)]
        res.append((math.fsum(addem)+1)/(1-dert[i]/math.factorial(i)))
    return res

def derTable(upper):
    res = [1,0,1]
    for i in range(3,upper):
        res.append((i-1)*(res[-1]+res[-2]))
    return res

def lolc(val,table):
    if val>100:
        return math.e
    else:
        return table[val]

def run(ctable):
    f=open("in.txt")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        terms = int(f.readline())
        cycTrack = [False for j in range(terms)]
        cycLens = []
        perm = map(int, f.readline().split())
        for j in range(terms):
            if cycTrack[j]:
                continue
            else:
                cycTrack[j]=True
                curLen = 1
                nextp = perm[j]-1
                while not cycTrack[nextp]:
                    curLen=curLen+1
                    cycTrack[nextp]=True
                    nextp=perm[nextp]-1
                cycLens.append(curLen)
        #grand = math.fsum([lolc(k,ctable) for k in cycLens])
        grand = sum(cycLens)-cycLens.count(1)
        g.write("%f\n" % grand)
    f.close()
    g.close()
    
    
