
def isr(u):
    u = str(u)
    ans = True
    for t in range(len(u)-1):
        if int(u[t + 1]) < int(u[t]):
            ans = False
            break
    return ans

def ooh(z):
    z = str(z)
    z = "0" + z
    l = len(z)
    new = int(z)
    for i in range(l - 1):
        if int(z[i + 1]) < int(z[i]):
            q = i
            f = l - i - 1
            k = str(int(z[i]) - 1)
            new = int(z[0:q] + k + "9" * f)
            break
    return new
T = int(raw_input())
for _ in range(T):
    z = raw_input()
    if int(z)<20:
        print "Case #%i: %i" % (_+1, int(z))
    else:
        while not isr(z):
            new = ooh(z)
            z = new
        print "Case #%i: %i" % (_ + 1, int(z))

