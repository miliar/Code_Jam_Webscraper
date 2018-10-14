# I have just learned python, so
# don't laugh...

teste = int(raw_input())

def gcd(a, b):
    if a<b:
        return gcd(b,a)
    if (b==0):
        return a
    return gcd(b, a%b)

for i in xrange(teste):
    buff = map(int, raw_input().split())
    nr = buff[0]
    elemente = buff[1:len(buff)]
    aaa = [0] * (nr-1);

    for j in xrange(nr-1):
        aaa[j] = abs(elemente[j+1]-elemente[j])

    g = reduce(gcd, aaa)

    if g==1:
        print "Case #%d: %s" % (i+1, 0)
    else:
        print "Case #%d: %s" % (i+1, (g - (elemente[1] % g))%g)

    

    
        
    
