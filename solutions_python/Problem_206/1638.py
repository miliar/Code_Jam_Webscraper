import sys

def slowride(t, ks):
    #t is total distance, subtract k from each t, then divide by s
    #find all linear intercepts, choose max time
    #get max time, div total dist by time, return
    times = []
    time_int = []
    for tup in ks:
        times.append( (t-tup[1])/tup[2] )
    for i, b1, k1 in ks[:-2]:
        for j, b2, k2 in ks[1:]:
            if k1 != k2:
                intercept = (b2-b1)/(k1-k2)
                if intercept < times[i] or intercept < times[j]:
                    times[i], times[j] = max(times[i], times[j])
    return t/max(times)


def main():
    with open(sys.argv[1], 'r') as infile:
        for i, line in enumerate(infile):
            if i == 0:
                continue
            t, n = line.strip().split()
            ks = []
            for j in range(0, int(n) ):
                ki, si = next(infile).strip().split()
                ks.append( (j, int(ki), int(si) ) )
            print("Case #" + str(i) + ": " + '{:f}'.format(slowride(int(t),ks)) )

if __name__ == "__main__":
    main()