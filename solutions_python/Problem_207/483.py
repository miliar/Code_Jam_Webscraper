def stable(s):
    N = int(s[0])
    R = int(s[1])
    Y = int(s[3])
    B = int(s[5])
    if R>Y+B or Y>R+B or B>Y+R:
        return 'IMPOSSIBLE'
    st = ''
    d = {}
    d['R']=R
    d['Y']=Y
    d['B']=B
    prev = max(d, key=d.get)
    mx = prev # maximum
    d[prev]=d[prev]-1
    st+=prev
    i = 0
    while i<N-1:
        m = max(d.keys(), key=lambda x: d[x] if not x==prev else 0)
        #print st,d, m
        d[m]=d[m]-1
        st+=m
        prev = m
        i+=1
        #adding one more mx
        if d[mx]>0 and prev!=mx and i<N-1:
            d[mx]=d[mx]-1
            st+=mx
            prev = mx
            i+=1
    #print st
    if st[0]==st[-1]:
        return 'IMPOSSIBLE'
    return st
f = open('input.in', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    tcs.append(f.readline().split(' '))

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, stable(tcs[i])))
f.close()

