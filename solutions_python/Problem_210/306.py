
def gcd(a,b):
    if a<b: return gcd(b,a)

    if a%b==0: return b
    return gcd(b,a%b)


def sol():
    t = int(raw_input())
    piii = 3.14159265358979323846
    for i in range(1,t+1):
        inp = list(map(int, raw_input().split()))
        n,k = inp[0],inp[1]
        arr = []

        for j in range(0,n):
            st = list(map(int, raw_input().split()))
            r,h = st[0],st[1]

            ar = 2*piii*r*h
            vals = {'a':ar,'s':piii*r*r,'r':r,'h':h}
            arr.append(vals)

        arr.sort(key=lambda tup: tup['a'])

        print arr


def sol():
    t = int(raw_input())
    
    for i in range(1,t+1):
        inp = list(map(int, raw_input().split()))
        ac,aj = inp[0],inp[1]
        sol = 2

        f1,f2,s1,s2=0,0,0,0
        if ac+aj>0:
            inp = list(map(int, raw_input().split()))
            f1,f2 = inp[0],inp[1]
        if ac+aj==2:
            inp = list(map(int, raw_input().split()))
            s1,s2 = inp[0],inp[1]

        if ac!=2 and aj!=2:
            sol=2
        else:
            dd = max(f2,s2) - min(f1,s1)
            ee = min(f2,s2) + 24*60- max(f1,s1)
            #print dd,ee
            if dd>720 and ee>720:
                sol=4


        print "Case #"+str(i)+": "+str(sol)

sol()
#sol()


