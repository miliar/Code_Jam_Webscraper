from math import sqrt as root

def palin(a):
    if str(a)==str(a)[::-1]:
        return True
    return False

f=open('C-small-attempt0.in','r')
g=open('b.out','w')

n = int(f.readline())
for x in range(n):
    print x,
    a = (f.readline()).split(' ')
    s,t = int(a[0]),int(a[1])
    p,q = int(root(s)),int(root(t))+1
    count = 0
    for i in range(p,q):
        if palin(i):
            sq = int(i**2)
            if palin(sq) and sq <= t and sq >= s:
                count = count + 1
                
    writ = 'Case #'+str(x+1)+': '+str(count)
    g.write(writ)
    g.write('\n')
g.close()
f.close()
        
