def foo(a):
    return a

ca = int(raw_input())
inm = map(foo, range(1, ca))
outm = map(foo, range(1, ca))
for ti in range(1, ca):
    in_string = raw_input()
    in_vector = in_string.split(" ")
    n = int(in_vector[0])
    m = int(in_vector[1])
    ans = 0
    while m is not 0:
        in_vector = in_string.split(" ")
        o = int(in_vector[0])
        e = int(in_vector[1])
        p = int(in_vector[2])
        inm(o) += p
        outm(e) += p
        ans=(ans+(n+n+1-(e-o))*(e-o)/2%mid*p)%mid
        m = m - 1
    for b in out:
        for a in inm:
            if a.ff>b.ff:
                break
        while b.ss>0:
            a = a-1
            mi=min(a.ss,b.ss);
            ans -= (n+n+1-(b.ff-a.ff))*(b.ff-a.ff)/2%mid*mi
            ans = (ans%mid+mid)%mid
            a.ss -= mi
            b.ss -= mi
    sys.stdout.write("Case #"+str(ti)+": "+str(ans)+"\n")