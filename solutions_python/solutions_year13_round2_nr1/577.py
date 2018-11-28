from sys import stdin as st

def g(a, b):
    if a == 1:
        return (100000001, 0)

    c = 0
    while a <= b:
        a += (a - 1)
        c += 1

    return (c, a)

cases = int(st.readline())

for case in xrange(1, cases + 1):

    a, n = [ int(x) for x in st.readline().split() ]
    m = [ int(x) for x in st.readline().split() ]
    m.sort()

    #print a
    #print m

    x = 0
    for k, v in enumerate(m):
        #print "index: %d, hodnota: %d" % (k, v)

        if a > v:
            #print "%d zje %d" % (a, v)
            a += v 
            continue

        #print "%d nezje %d" % (a, v)

        toend = len(m) - k
        c, na = g(a, v)

        #print "toend: %d, c: %d, na: %d" % (toend, c, na)

        if toend <= c:
            x += toend
            break  
        
        a = na
        a += v
        x += c

    print "Case #%d: %d" % (case, x)


