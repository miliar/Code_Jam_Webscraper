l = []
def numEuro(r, k, n):
    num = 0
    
    for x in range(r):
        ll = []
        sum = 0
        
        while (l):
            if(sum + l[0] > k):
                break
            sum = sum + l[0]
            ll.append(l.pop(0))
        
        num = sum + num
        l.extend(ll)
                  
    return num
    
cfile = open('C.in','r')
numTestCase = int(cfile.readline())

outfile = open('C.out','w')

i = 0
while i<numTestCase:
    i = i + 1
    s1 = cfile.readline().strip('\n')
    r1, k1, n1 = [int(z) for z in s1.split(' ')]
    
    s2 = cfile.readline().strip('\n')
    l = [int(ll) for ll in s2.split(' ')] 
    
    outfile.write('Case #{0}: {1}\n'.format(i, numEuro(r1, k1, n1)))
    
cfile.close()    
outfile.close()       