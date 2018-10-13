import sys

with open(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for t in range(T):
        print "Case #%s:" % (t+1),
        N, L, H = [int(x) for x in f.readline().strip().split()]
        frequencies = [int(x) for x in f.readline().strip().split()]
        for ff in range(L, H+1):
            for freq in frequencies:
                if freq%ff and ff%freq:
                    break
            else:
                print ff
                break
        else:
            print "NO"
