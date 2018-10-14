t = int(input())

for i in range(t):
    n,r,o,y,g,b,v = map(int,raw_input().strip().split())

    l = [r,y,b]
    s = [str(r)+'R',str(y)+'Y',str(b)+'B']
    l.sort()
    if l[0]+l[1]<l[2]:
        ans = "IMPOSSIBLE"
    else:
        s.sort()
        ss=list()
        m1=int(s[1][:-1])
        m2=int(s[2][:-1])
        for j in range(int(s[1][:-1])+int(s[2][:-1])):
            if m2!=0:
                ss.append(s[2][-1])
                m2-=1
            if m1!=0:
                ss.append(s[1][-1])
                m1-=1
        if int(s[0][0])>0:
            ss.append(s[0][-1])
        z=0
        for k in range(int(s[0][:-1])-1):
            z+=(-2)
            ss.insert(z,s[0][-1])
        ans = "".join(ss[x] for x in range(len(ss)))        
    print "Case #%d: "%(i+1)+ans
