import string

fin = open ( 'A-large.in', 'r' )
fout = open ( 'A-large.out', 'w' )

T = int(fin.readline ( ))

def add ( d, paths ):
    counter = 0
    dd = d
    for path in paths:
        if path not in dd:
            dd[path] = {}
            counter = counter+1
        dd = dd[path]
    return counter

for t in range(1,T+1):
    dict = {}
    elem = string.split ( fin.readline(), ' ' )
    n = int(elem[0])
    m = int(elem[1])
    result = 0
    for i in range(n):
        elem = fin.readline()[:-1].split ( '/' )
        add ( dict, elem[1:] )
    for i in range(m):
        elem = fin.readline()[:-1].split ( '/' )
        result += add ( dict, elem[1:] )

    print 'Case #%d: %d' % ( t, result )
    fout.write ( 'Case #%d: %d\r\n' % ( t, result ) )

fout.close()