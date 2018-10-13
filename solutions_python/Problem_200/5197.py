def test(N):
    for i in range(N,0,-1):
        if sorted(`i`)==list(`i`):
            return i

r=open('inp.txt','r').read().splitlines()
w=open('out.txt','w')
for i,n in enumerate(r[1:]):
    w.write("Case #%s: %s"%(i+1,str(test(int(n)))))
    w.write('\n')
