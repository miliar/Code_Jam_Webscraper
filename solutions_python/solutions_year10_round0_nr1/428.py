def switch(a,b):
    s = bin(k).lstrip('0b')
    if(len(s) < n):
        return 'OFF'
    if('0' in s[-n:]):
        return 'OFF'
    else:
        return 'ON'
    
    
afile = open('A.in','r')
numTestCase = int(afile.readline())

outfile = open('A.out','w')
i = 0
while i<numTestCase:
    i = i + 1
    s1 = afile.readline().strip('\n')
    n,k = [int(l) for l in s1.split(' ')]

    outfile.write('Case #{0}: {1}\n'.format(i, switch(n,k)))
    
afile.close()    
outfile.close()    