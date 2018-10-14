from fractions import Fraction

def readInts():
    return [int(x) for x in raw_input().strip().split()]
    
n = readInts()[0]
for i in xrange(n):
    res = ""
    [n,pd,pg] = readInts()
    tmp = map(int,str(Fraction(pd,100)).split('/'))
    if len(tmp)==1:
	tmp.append(1)
    [numer,denom] = tmp
    if (denom > n):
	print "Case #%d: Broken"%(i+1)
    elif (pg==100 and pd!=100):
	print "Case #%d: Broken"%(i+1)
    elif (pg==0 and pd!=0):
	print "Case #%d: Broken"%(i+1)
    else:
	print "Case #%d: Possible"%(i+1)
    
	