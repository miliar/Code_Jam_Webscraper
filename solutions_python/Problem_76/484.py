import sys, itertools

def precandysplit( line ):
    line = [ int(a) for a in line ]
    line.sort(reverse = True)
    return candysplit( line )

def candysplit( candy ):
    if xorsum( candy ) != 0:
        return "NO"
    for i in range( 1, len(candy)/2 + 1 ):
        l = len(candy) - i
        if xorsum( candy[0:-i] ) == xorsum( candy[-i:] ):
            return sum( candy[0:-i])
        '''
        for c in itertools.combinations( candy, l ):
            rest = candy[:]
            for a in c:
                rest.remove(a)
            #print c, rest
            #print xorsum( c ), xorsum( rest)
            if xorsum( c ) == xorsum( rest ):
                #print c, cset.difference(c)
                #print xorsum( c ), xorsum( cset.difference(c) )
                return sum( c )
        '''
    return "NO"

def xorsum( c ):
    i = 0
    for a in c:
        i ^= a
    return i
    

T = int( sys.stdin.readline().strip() )

case = 0
for i in range(T):
    candies = int( sys.stdin.readline().strip() )
    line = sys.stdin.readline().strip().split(" ")
    case += 1
    print "Case #%s: %s" % ( case, precandysplit( line ) )
