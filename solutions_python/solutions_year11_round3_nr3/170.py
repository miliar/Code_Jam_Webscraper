fi = open('C-small-attempt1 (2).in','r')
fo = open('out.txt','w')
n = int(fi.readline().split()[0])
for i in range(n):
    a,b,c = map(int,fi.readline().split())
    m = map(int,fi.readline().split())
    t=True
    ans = 0
    for j in range(b,c+1):
        for k in m:
            if k%j != 0 and j%k != 0:
                t=False
                break
        if t:
            ans=j
            break
        else:
            t=True
    if ans > 0:
        fo.write('Case #%d: %d\n' % (i+1,ans))
    else:
        fo.write('Case #%d: NO\n' % (i+1))
fo.close()
        
                
