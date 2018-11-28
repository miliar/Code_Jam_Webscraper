import sys
sys.setrecursionlimit(10000000)

cases = int(raw_input())

def cookieBuy(rate,factoryPrice,target,factoryRate, curSec):
    asec = curSec
    asec += target / rate
    
    bsec = curSec
    bsec += factoryPrice / rate    
    rate += factoryRate  
    bsecBak = bsec  
    bsec += target / rate
    
    if (asec <= bsec):
        return asec
    else:
        return cookieBuy(rate,factoryPrice,target,factoryRate,bsecBak)

for case in range(1,cases+1):
    inp = raw_input()
    factoryPrice, factoryRate, target = map(float,inp.split(" "))
    
    sec = cookieBuy(2,factoryPrice,target,factoryRate,0)
    
    print "Case #%i: %s" % (case,sec)
