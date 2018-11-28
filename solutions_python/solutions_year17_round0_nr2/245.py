# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# nb tests
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N=raw_input()
    L=len(N)
    cd=0
    tm=0
    b=0
    dead=False
    
    for k in range(L):
        if dead:
            tm=tm*10
        else:
            d=int(N[k])
            cd=10*cd+d
            if d>b:
                tm=cd
            elif d==b:
                tm*=10
            else:
                tm*=10
                dead=True
#        print k,b,d,dead,cd,tm
        b=d
    if dead:
        res=tm-1
    else:
        res=cd
    print "Case #{}: {}".format(i,res)
