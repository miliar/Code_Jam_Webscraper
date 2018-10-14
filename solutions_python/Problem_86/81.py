import sys

def solve(notes, lo, hi, casen):
    sol = 0
    for i in xrange(lo, hi+1):
        valid = True
        for n in notes:
            if i % n != 0 and n % i != 0:
                valid = False
                break
        if valid:
            sol = i
            break
    print "Case #%d: %s" % (casen, str(sol) if sol else 'NO')
                
if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as f:
        lines = f.readlines()
        ncases = int(lines[0])
        lines = lines[1:]
        for i in xrange(ncases):
            n, l, h = map(int, lines[0].strip().split(' '))
            notes = map(int, lines[1].strip().split(' '))
            lines = lines[2:]
            solve(notes, l, h, i+1)
