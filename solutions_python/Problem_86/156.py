import sys

def read_string():
    return sys.stdin.readline().strip()

def read_strings():
    return read_string().split()

def read_integer():
    return int( read_string() )

def read_integers():
    return [ int( x ) for x in read_strings() ]

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    N, L, H = read_integers()
    notes = read_integers()
    success = False
    for trial in range( L, H + 1 ):
        failure = False
        for n in notes:
            if trial % n == 0 or n % trial == 0:
                continue
            failure = True
        if not failure:
            print trial
            success = True
            break
    if not success:
        print 'NO'
