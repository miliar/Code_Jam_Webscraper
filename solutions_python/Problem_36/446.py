# Python 2.5.4
# SMALL INPUT: program.py < A.small.in > A.small.out
# LARGE INPUT: program.py < A.large.in > A.large.out
pattern = "welcome to code jam"
case = None
base = 10000

def add(a, b):
    return (a % base + b % base) % base

def proc(p, s):
    if (len(p) == 0) or (len(s) == 0):
        return 0

    if len(p) == 1:
        return s.count(p)

    l = [proc(p[1:], s[x + 1:]) for x in range(0, len(s)) if s[x] == p[0]]
    if (len(l) == 0):
        return 0;

    if (len(l) == 1):
        return l[0]

    return reduce(add, l)
    

def main():
    N = input()    

    for i in xrange(0, N):
        case = raw_input()
        print "Case #%d: %04d" % (i + 1, proc(pattern, case))

if __name__ == '__main__':
    main()

    
