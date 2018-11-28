#!/usr/bin/python

def solve(d, n, horses, speeds):
    maxTime = float('-inf')
    for i, pos in enumerate(horses):
        dist = d - pos
        time = 1.0 * dist / speeds[i]
        if time > maxTime:
            maxTime = time
    return 1.0 * d / maxTime

def main():
    t = int(raw_input())
    for i in xrange(t):
        d, n = map(int, raw_input().split(" "))
        horses = []
        speeds = []
        for j in xrange(n):
            k, s = map(int, raw_input().split(" "))
            horses.append(k)
            speeds.append(s)
        res = solve(d, n, horses, speeds)
        print "Case #{}: {}".format(i+1, res)

if __name__ == '__main__':
    main()
