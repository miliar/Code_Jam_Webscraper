
def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        D,  N = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        maxtime = None
        for j in xrange(N):
            Kj, Sj = [int(s) for s in raw_input().split(" ")]
            time = (D-Kj)/float(Sj)
            if maxtime is None or time > maxtime: 
                maxtime = time
            
        print "Case #{}: {}".format(i, D/maxtime)

if __name__ == "__main__":
    main()
