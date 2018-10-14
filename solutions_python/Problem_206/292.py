import sys



if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for i in xrange(t):
    	d, n = f.readline().split()
    	d = int(d)
        n = int(n)

        max_time = 0

        for j in range(n):
            k, s = f.readline().split()
            k = float(k)
            s = float(s)

            dist = d-k
            time = dist / s

            max_time = max(time, max_time)

        max_speed = d/max_time
		
        print("CASE #{0}: {1}".format(i+1, max_speed))