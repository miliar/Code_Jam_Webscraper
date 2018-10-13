import sys
import math

def run(R, K, N, groups):
    # R: rounds
    # K: space
    # N: # groups
    Q = groups[:]
    fee = 0
    for i in range(R):
        car = []
        while Q and Q[0] <= K - sum(car):
            next = Q.pop(0)
            car.append(next)
        fee += sum(car)
        Q = Q + car
    return fee

def main(filename):
    f = open(filename)
    T = int(f.readline())
    for i in range(1, T+1):
        line = f.readline()
        terms = line.split()
        R = int(terms[0])
        K = int(terms[1])
        N = int(terms[2])
        line = f.readline()
        groups = [int(x) for x in line.split()]
        assert len(groups) == N, groups
        res = run(R, K, N, groups)
        print "Case #%d: %s" % (i, res)
    f.close()
    

if __name__ == '__main__':
    main(sys.argv[1])