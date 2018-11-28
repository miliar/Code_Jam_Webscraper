import sys

def main(input):
    T = int(input.readline())

    for i in range(T):
        print "Case #%s:"% (i+1),

        N = int(input.readline())
        vs = []
        xs = set()
        for n in range(N):
            v = input.readline().strip()

            c = []
            last_char = None
            count = 0
            for i in v:
                if last_char  == None:
                    count = 1
                    last_char = i
                elif last_char == i:
                    count += 1
                else:
                    c.append((last_char, count))
                    last_char = i
                    count = 1

            c.append((last_char, count))
            vs.append(c)

            # print c
            x = reduce(lambda i, j: i if i[-1] == j else i+j, v)

            xs.add(x)

        if len(xs) != 1:
            print 'Fegla Won'
            continue

        key = xs.pop()

        # print c
        step = 0
        for k in xrange(len(key)):
            cv = [v[k][1] for v in vs]

            avg = sum(cv) / len(vs)
            step += sum(abs(k -avg) for k in cv)
            # print cv, avg, step

        print step



main(sys.stdin)
