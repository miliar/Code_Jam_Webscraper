

f = '/Users/larsr/Downloads/C-small-attempt0 (1).in'
f = '/Users/larsr/Downloads/C-small-attempt0.in'
f = '/Users/larsr/Downloads/C-small-attempt1.in'
f = '/Users/larsr/Downloads/C-large.in'
data=open(f).read().split('\n')

N = int(data[0])

w = file('/Users/larsr/out2.txt','w')

li = []

for i in range(N):
    n,m = [int(x) for x in data[i+1].split()]
    #n,m = 100,500
    #n,m = 1111,2222
    #n,m = 200,2000000
    c = 0

    for x in range(n,m+1):
        s =str(x)
        ss = [x]
        for j in range(1,len(s)):
            if s[j]!='0':
                s2=int(s[j:]+s[:j])
                #print s2>x, s2<m,x,s2
                if s2>x and s2<=m and not s2 in ss:
                    ss.append(s2)
                    #li.append((x,s2))
        if min(ss)==x:
            c += len(ss)-1
    print 'Case #%d (%d,%d):'%(i+1,n,m),c
    w.write('Case #%d: %d\n'%((i+1),c))

w.close()    
