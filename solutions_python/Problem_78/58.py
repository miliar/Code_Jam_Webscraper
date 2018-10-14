IN = 'A-large.in'
OUT = 'a.out'

with open(IN, 'r') as fin:
    with open(IN + '.out.txt', 'w') as fout:
        T = int(fin.readline())

        for case in xrange(1, T + 1):
            what = "Broken"
            N, Pd, Pg = map(int, fin.readline().split())

            for i in xrange(1, min(101, N + 1)):
#                print Pd * i
                if (Pd * i) % 100 == 0:
                    what = "Possible"
            if (Pg == 100 and Pd != 100) or (Pg == 0 and Pd != 0):
                what = "Broken"

            fout.write("Case #%d: %s\n" % (case, what))
        
