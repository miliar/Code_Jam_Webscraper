def mult(a, b):
    return (a/abs(a))*(b/abs(b))*[[1, 2, 3, 4], [2, -1, 4, -3], [3, -4, -1, 2], [4, 3, -2, -1]][abs(a)-1][abs(b)-1]
    
for t in xrange(1, input()+1):
    m, n = map(int, raw_input().split())
    s = map(lambda x: {'1':1, 'i':2, 'j':3, 'k':4}[x], raw_input())*n
    a = reduce(lambda x,y: x+[mult(x[-1], y)], s, [1])[1:]
    print 'Case #%d: %s'%(t, 'YES' if a[-1] == -1 and 2 in a and 4 in a[a.index(2):] else 'NO')