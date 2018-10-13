def main():
    t = int(raw_input())
    for i in xrange(t):
        can = True
        lin = {}
        col = {}
        a = {}
        b = {}
        first = raw_input()
        line = first.split(" ")
        n = int(line[0])
        m = int(line[1])
        for j in xrange(n):
            lin[j] = 0
        for j in xrange(m):
            col[j] = 0
        for j in xrange(n):
            a[j] = {}
            b[j] = {}
            string = raw_input()
            line = string.split(" ")
            for k in xrange(len(line)):
                a[j][k] = int(line[k])
                if a[j][k] > lin[j]:
                    lin[j] = a[j][k]
                if a[j][k] > col[k]:
                    col[k] = a[j][k]
                b[j][k] = 100
        for j in xrange(n):
            for k in xrange(m):
                if b[j][k] > lin[j]:
                    b[j][k] = lin[j]
                if b[j][k] > col[k]:
                    b[j][k] = col[k]
        for j in xrange(n):
            for k in xrange(m):
                if b[j][k] != a[j][k] or can == False:
                    can = False
                    break
        if can:
            print "Case #%s: YES" % (i + 1)
        else:
            print "Case #%s: NO" % (i + 1)

main()
