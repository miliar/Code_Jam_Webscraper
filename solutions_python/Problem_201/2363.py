## bathroom small

import math


f= open('C-small-2-attempt0.in','r')
fout = open('C-small-2-attempt0-result.txt','w')

#f= open('test.txt','r')
#fout = open('test-result.txt','w')

casenum = int(f.readline())

for i in range(casenum):
    info = f.readline()
    n = int(info.split(' ')[0])
    k = int(info.split(' ')[1])
    digit = int(math.log(k,2))+1
    m = 2**(digit-1)
    z = int((n+1)/m+1) if((n+1)%m > (k-m)) else int((n+1)/m);
    
    lrmax = int((z-1)/2)
    lrmin = int(z/2)-1
    output = 'Case #' + str(i+1)+': '+str(lrmax)+' '+str(lrmin)
    fout.write(output)
    fout.write('\n')

fout.close()
