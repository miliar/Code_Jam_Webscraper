import collections

def read_line():
    return raw_input().strip()

def read_words():
    return read_line().split()

def read_integer():
    return int( read_line() )

def read_integers():
    return [ int( x ) for x in read_words() ]

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 )
    S = read_integers()
    N = S.pop( 0 )
    sums = collections.defaultdict( set )
    start = 2**19
    found = None
    for index in range( 2**N ):
        bit = start
        offset = N - 1
        total = 0
        while bit:
            if index & bit:
                total += S[ offset ]
            bit >>= 1
            offset -= 1
        for check in sums[ total ]:
            if index & check == 0:
                found = index, check, total
                break
        if found:
            break
        sums[ total ].add( index )
    if found:
        for index in found[ : 2 ]:
            bit = start
            offset = N - 1
            while bit:
                if index & bit:
                    print S[ offset ],
                bit >>= 1
                offset -= 1
            print
    else:
        print 'Impossible'
