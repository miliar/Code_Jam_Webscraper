from fractions import gcd

l = []
def FairWarn():
    ll = sorted(list(set(l[1:])))
    diff = list({y-x for x in ll for y in ll if y > x})
    if  len(diff) == 0:
        return 0
        
    if(len(diff) == 1):
        g = diff[0]
    elif (len(diff) == 2):
        g = gcd(diff[0],diff[1])
    else:
        g = gcd(diff[0], diff[1])
        g = gcd(diff[2], g)
    
    return (g - (ll[0] % g)) % g 

    
cfile = open('B.in','r')
numTestCase = int(cfile.readline())

outfile = open('B.out','w')

i = 0
while i<numTestCase:
    i = i + 1
    s1 = cfile.readline().strip('\n')
    l = [int(ll) for ll in s1.split(' ')]
    outfile.write('Case #{0}: {1}\n'.format(i, FairWarn()))
    
cfile.close()    
outfile.close()       