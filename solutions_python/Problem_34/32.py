import sys

def main(fname):
    f = open(fname)

    l,d,n = [int(s) for s in f.readline().split()]

    words = [f.readline().strip() for _i in xrange(d)]

    messages = [f.readline().strip() for _i in xrange(n)]

    for i in xrange(n):
        print "Case #%d:" % (i+1),
        total = 0

        m = messages[i]

        sets = []
        cur = 0
        while len(sets) < l:
            if m[cur] != '(':
                sets.append(set([m[cur]]))
                cur += 1
            else:
                s = set([])
                cur += 1
                while m[cur] != ')':
                    s.add(m[cur])
                    cur += 1
                cur += 1
                sets.append(s)

        for j in xrange(d):
            for k in xrange(l):
                if not words[j][k] in sets[k]:
                    break
            else:
                total += 1

        print total
        # print sets

    f.close()

if __name__ == "__main__":
    main(sys.argv[1])
