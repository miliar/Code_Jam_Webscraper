import sys

def find_wanted_speed(horses, D):
    max_time = 0
    for k, s in sorted(horses, reverse=True):
        arrival = float(D - k) / s
        if arrival > max_time:
            max_time = arrival
    return D / max_time


if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        D, N = [int(part) for part in sys.stdin.readline().split()]
        horses = []
        for _ in xrange(N):
            K, S = [int(part) for part in sys.stdin.readline().split()]
            assert K < D
            horses.append((K, S))
        speed = find_wanted_speed(horses, D)
        print "Case #%d: %f" % (i+1, speed)
