def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a%b)

of = open("B-large.in", "r")
data = of.read()
of.close()

datal = data.split("\n")

T = int(datal[0])

for t in range(1, T+1):
    case = datal[t].split(" ")

    N = int(case[0])
    n = []
    for i in range(1, N+1):
        n.append(int(case[i]))
    n.sort()

    dif = []
    for i in range(1, N):
        dif.append(n[i]-n[i-1])

    d = dif[0]
    for i in range(1, len(dif)):
        d = gcd(d, dif[i])

    print "Case #" + `t` + ":",
    if n[0]%d == 0: print 0
    else: print (n[0]/d + 1)*d - n[0]
