import StringIO, sys, math

if len(sys.argv)>1:
    input = file(sys.argv[1])
else:
    input = StringIO.StringIO("""4
1 9
10 40
100 500
1111 2222""")


def variants(n, d, f):

    v = set([n])
    for x in range(d):
        n = f*(n%10)+n/10
        v.add(n)

    return v

def check(a, b):
    d = int(math.log(a, 10))
    f = 10**d
    c = 0
    for n in range(a, b):
        v = variants(n, d, f)
        for m in range(n+1, b+1):
            if m in v:
                c+=1
                m = m + 9 - m%10
                #print "n:%d und m:%d are recycled!" % (n, m)
    return c

for case in range(int(input.readline())):
    a, b = [int(x) for x in input.readline().split()]
    print "Case #%d: %d" % (case+1, check(a, b))

