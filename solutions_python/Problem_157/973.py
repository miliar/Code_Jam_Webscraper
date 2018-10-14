operations = [
('1', '1', ('+', '1')),
('1', 'i', ('+', 'i')),
('1', 'j', ('+', 'j')),
('1', 'k', ('+', 'k')),
('i', '1', ('+', 'i')),
('i', 'i', ('-', '1')),
('i', 'j', ('+', 'k')),
('i', 'k', ('-', 'j')),
('j', '1', ('+', 'j')),
('j', 'i', ('-', 'k')),
('j', 'j', ('-', '1')),
('j', 'k', ('+', 'i')),
('k', '1', ('+', 'k')),
('k', 'i', ('+', 'j')),
('k', 'j', ('-', 'i')),
('k', 'k', ('-', '1')),
]

operations_table = {}
for lval, rval, result in operations:
    try:
        operations_table[lval][rval] = result
    except KeyError:
        operations_table[lval] = {rval: result}

def red(l, r):
    lsign, lval = l
    rsign, rval = r
    if lsign == rsign:
        return operations_table[lval][rval]
    else:
        resign, reval = operations_table[lval][rval]
        return ({'+':'-','-':'+'}[resign], reval)

#inp = 'ijk'
import random
#inp = ""
#for i in xrange(0, random.randint(9000,10000)):
#    inp += random.choice('ik')

def sol(piece, times):
    inp = piece * times
    n = len(inp)

    #si = sj = sk = 0
    #px = piece*2
    #lp = len(px)
    #a = ('+', px[0])
    #j = 1
    #print a
    #while j < lp:
    #    a = red(a, ('+', px[j]))
    #    print a
    #    j += 1
    #print si, sj, sk
    #if si+sj+sk != 3:
    #    return False

    lx = -1
    x = 0
    try:
        # adjust x
        while 1:
            a = ('+', inp[x])
            while x < n:
                if a == ('+', 'i') and x > lx:
                    break
                x += 1
                a = red(a, ('+', inp[x]))
            lx = x
            y = x + 1
            a = ('+', inp[y])
            # adjust y
            ly = -1
            while ly + 1 < n:
                while y < n:
                    if a == ('+', 'j') and y > ly:
                        break
                    y += 1
                    a = red(a, ('+', inp[y]))
                ly = y
                z = y + 2
                a = ('+', inp[z - 1])
                while z < n:
                    a = red(a, ('+', inp[z]))
                    z += 1

                if a == ('+', 'k'):
                    ##print inp[0:x+1]
                    ##print inp[x+1:y+1]
                    ##print inp[y+1:]
                    return True
    except IndexError:
        return False
    return False

#inp = 'kj'*10000
fp = open("3.in")
tests = int(fp.readline())
for i in range(tests):
    l, x = fp.readline().split()
    x = int(x)
    s = fp.readline().strip()
    print "Case #%d: %s" % (i+1, ["NO", "YES"][sol(s, x)])


