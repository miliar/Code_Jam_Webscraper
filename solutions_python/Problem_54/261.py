def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

cases = int(raw_input())
for i in range(1,cases+1):
    print "Case #"+str(i)+":",
    t = map(int,raw_input().split(" ")[1:])
    g = 0
    for i in t:
        for j in t:
            if i>j:
                g = gcd(g, i-j)
    result = (-t[0])%g
    if result<0:
        result += g
    print result
    

