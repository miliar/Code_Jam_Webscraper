import sys

def linea():
    return sys.stdin.readline()

def lee(j):
    for i in xrange(1,5):
        nrs = [int(w) for w in linea().split()]
        if i == j:
           keep = nrs

    return keep

def solve():
    user1 = int(linea())
    keep1 = lee(user1)
    user2 = int(linea())
    keep2 = lee(user2)

    # cuantas veces hay nros de keep1 en keep2?
    common = [ x for x in keep1 if x in keep2 ]
    c = len(common)
       
    if c == 0: # no hay manera de elegir
       return 'Volunteer cheated!'

    if c > 1: # mas de 1 opcion
       return 'Bad magician!'

    # la unica opcion
    return "%d" % common[0]


# main()

# read 1 number, use it to control the loop
for tc in xrange(1, int(sys.stdin.readline())+1):
    # read 2 numbers
    sol = solve()

    print 'Case #%d: %s' % (tc,sol)
