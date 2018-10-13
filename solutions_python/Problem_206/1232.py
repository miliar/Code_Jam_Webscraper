import sys
import math

def compute_opt_speed(D, times):
    times.sort(reverse=True)
    stime = times[0]

    return D/stime

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        case = 0
        T = int(f.readline().strip())
        for case in range(1,T + 1):
            line = f.readline().split(" ")
            D = int(line[0])
            N = int(line[1])
            times = []
            for i in range(N):
                l = f.readline().split(" ")
                k = float(l[0])
                s = float(l[1])
                times.append((D - k)/s)
            speed = compute_opt_speed(D, times)
            print "Case #%s: %s" % (case, speed)
