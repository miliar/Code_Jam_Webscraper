DEFAULT_DATA = '''2
3
1 10
5 5
7 7
2
1 1
2 2
'''

def run(data):
    count = int(data.readline())
    i = 0
    while i < count:
        i += 1
        n = int(data.readline())
        wires = []
        for x in range(0,n):
            a1,a2 = [int(x) for x in data.readline().split(' ')]
            wires.append( (a1,a2) )
            #print 'Case #%d: %s' % (i, 'ON' if k&(2**n-1) == 2**n-1 else 'OFF')
        ix = 0
        while wires:
            a0,a1 = wires.pop()
            c = len([ (x[1]-a1)/(x[0]-a0) for x in wires if (x[1]-a1)/(x[0]-a0) < 0])
            ix += c
        print 'Case #%s: %s' % (i,ix)

if __name__ == "__main__":
    import sys, cStringIO
    if len(sys.argv) == 1:
        data = cStringIO.StringIO(DEFAULT_DATA)
    else:
        data = open(sys.argv[1])
    run(data)
