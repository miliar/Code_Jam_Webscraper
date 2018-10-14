for tc in range(1,int(raw_input())+1):
    d,k = map(int,raw_input().split())
    p=[0]*k
    s=[0]*k
    for i in range(k):
        p[i],s[i]=map(int,raw_input().split())
    t=[0.]*k
    for i in range(k):
        t[i]=float(float(d-p[i])/float(s[i]))
    mx=float(max(t))
    print('Case #'+str(tc)+': %.6f'%float(d/mx))
