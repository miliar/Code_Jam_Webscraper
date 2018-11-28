def rotate(s, i):
    return s[i:] + s[:i]

def solve(a, b):
    # TODO: cache / prepare pairs in advance
    
    c = 0
    for i in xrange(int(a), int(b) + 1):
        s = str(i)
        l = []
        for j in xrange(len(s) - 1):
            ss = rotate(s, j + 1)
            if s < ss and a <= ss <= b and ss not in l:
                l.append(ss)
                c += 1

    return c

# This takes 5 seconds: print solve("1000000", "2000000")

if __name__ == "__main__":

    count = int(raw_input())
    for i in range(count):
        a, b = raw_input().split(" ")
        print 'Case #%d: %s' % ((i+1), solve(a, b))
