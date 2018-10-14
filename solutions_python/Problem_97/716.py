import sys, string

def recycle(a, b):
    ndigits = len(str(b))
    shifter = int(10**(ndigits-1))
    cnt = 0
#    print "testing", a, b
    for n in range(a, b):
#        print "checking", n
        m = n
        h = m / shifter
        seen = {}
        for s in range(1, ndigits):
            m = (m % shifter)*10 + h
            h = m / shifter
#            print "m", m
            if h and n < m and m >= a and m <= b and not m in seen:
#                print n, m
                seen[m] = 1
                cnt += 1 
    return cnt

def main(args):
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline()
        line = line.rstrip()
        parts = line.split()
        nums = map(int, parts)
        a, b = nums[0:2]
        ans = recycle(a, b)
        sys.stdout.write("Case #%d: %d\n" % (i+1, ans))

if __name__ == "__main__":
    main(sys.argv)