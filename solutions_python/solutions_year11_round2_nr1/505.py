import string
import sys


def wp(s):
    wp = 1.0*len(s.replace(".","").replace("0",""))/len(s.replace(".",""))
    return wp
    
def owp(x,k,N):
    countOponents = 0;
    wpSum = 0;
    xt = x[:]
    xt.remove(xt[k])
    for i in range(N-1):
        if(xt[i][k] != "."):
            countOponents += 1
            wpSum += 1.0*wp(xt[i].replace(xt[i][k],"",1))
    if(countOponents !=0):
        owp = 1.0*wpSum/countOponents   
        return  owp
    else:
        return 0
        
def oowp(x,k,N):
    countOponents = 0;
    owpSum = 0;
    xt = x[:]
    xt.remove(xt[k])
    for i in range(N-1):
        if(xt[i][k] != "."):
            countOponents += 1
            if(i<k):
                owpSum += owp(x,i,N)
            else:
                owpSum += owp(x,i+1,N)
    if(countOponents !=0):
        oowp = 1.0*owpSum/countOponents
        return oowp
    else:
        return 0
    



f =open(sys.argv[1],"r")
T =int(f.readline())

for i in range (T):
    print "Case #{0}:".format(i+1)
    N= int(f.readline())
    x = []
    for j in range(N):
        inp = f.readline()
        x.append(inp.replace("\n",""))
    for k in range(N):
        RPI = 0.25*wp(x[k])+0.5*owp(x,k,N)+0.25*oowp(x,k,N)
        print RPI
