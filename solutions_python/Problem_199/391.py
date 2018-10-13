#!/usr/bin/python

def solve(pancakes, k):
    states = list(pancakes)
    pos = 0
    numPancakes = len(states)
    count = 0
    while pos + k - 1 < numPancakes:
        if states[pos] == '-':
            count += 1
            for i in range(k):
                states[pos+i] = '+' if states[pos+i] == '-' else '-'
        pos += 1

    for i in range(k-1):
        if states[pos+i] == "-":
            return -1
    return count

def main():
    t = int(raw_input())
    for i in xrange(t):
        testStr, kstr = raw_input().split(" ")
        res = solve(testStr, int(kstr))
        print "Case #{}: {}".format(i+1, "IMPOSSIBLE" if res < 0 else res)

if __name__ == '__main__':
    main()
