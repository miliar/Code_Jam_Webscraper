import math
def isPal(st):
    for i in range(len(st)/2):
        if st[i]!=st[len(st)-1-i]:
            return False
    return True

fi = open('C-small-attempt0.in','r')
fo = open('C-small-attempt0.out','w')

n = int(fi.readline())
for t in range(n):
    count = 0
    inds = fi.readline().split()
    a = int(math.ceil(math.sqrt(float(inds[0]))))
    b = int(math.trunc(math.sqrt(float(inds[1]))))
    for i in range(a, b+1):
        if isPal(str(i)) and isPal(str(i*i)):
            count += 1
    fo.write('Case #'+str(t+1)+': '+str(count)+'\n')

fi.close()
fo.close()