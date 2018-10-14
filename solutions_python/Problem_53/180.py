import sys

sys.stdin.readline()
count = 1
for line in sys.stdin:
    a, b = map( int, line.split( ' ' ) )
    if (b & ((1<<a) - 1)) == ((1<<a) - 1) :
        print 'Case #%d: ON' % count
    else:
        print 'Case #%d: OFF' % count
    count += 1

    
