"""
QR2011 C
http://code.google.com/codejam/contest/dashboard?c=975485#s=p2
"""

def Patrick(a, b):
    a = "%024d" % int(format(a, 'b'))
    b = "%024d" % int(format(b, 'b'))
    c = "".join([ str(int(a[i])^int(b[i])) for i in range(24) ])
    return int(c, 2)

if __name__ == "__main__":
    f = open("C-large.in")
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        C = [ int(x) for x in f.readline().split() ]
        result = ""
        if reduce(Patrick, C):
            result = "NO"
        else:
            result = str(sum(sorted(C)[1:]))
        print "Case #%d: %s" % (t+1, result)
