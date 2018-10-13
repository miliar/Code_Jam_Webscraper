s = set()
T = int(raw_input())
def getNum(n):
    if n == 0:
        s.add(0)
    else:
        while n>0:
            s.add(n%10)
            n/=10

for i in xrange(T):
    s = set()
    N = int(raw_input())
    if N == 0:
        print "Case #"+str(i+1)+": INSOMNIA"
        continue
    cnt = 1
    k = N
    while len(s) < 10:
        getNum(k)
        cnt+=1
        k = cnt*N

    print "Case #"+str(i+1)+": "+ str(N*(cnt-1))
