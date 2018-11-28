import sys

N = int(sys.stdin.readline())
count = 0

for i in xrange( N ):
    count += 1
    loop, k, n = map( int, sys.stdin.readline().split( ' ' ) )
    gr = map( int, sys.stdin.readline().split( ' ' ) )

    j = 0
    cur = gr[0]
    euro = 0
    st = 0
    while loop:
        j = (j + 1) % len( gr )
        c = gr[j]
        if st != j and cur + c <= k:
            cur += c
        else:
            euro += cur
            st = j
            cur = c
            loop -= 1
            
    print 'Case #%d: %d' % (count, euro)
    
