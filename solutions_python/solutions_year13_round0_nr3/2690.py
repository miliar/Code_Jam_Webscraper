import sys
f=open('C-small-attempt0.in')
output=open('C-small-attempt0.out','w')
cases = int(f.readline())
squareprimes=[1,4,9,121,484,10201,12321,14641,40804,44944,1002001]
for t in range(cases):
    inlin=(f.readline()).split()
    a=int(inlin[0])
    b=int(inlin[1])
    incount=0
    for i in squareprimes:
        if a<=i and b>=i:
            incount+=1
        if b <i:
            break
    
    output.write('Case #'+str(t+1)+': '+str(incount)+'\n')
f.close()
output.close()
