#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(1, n+1):
        line = sys.stdin.readline()[:-1]

        print 'Case #{0}: {1}'.format(i, dancing(line))

def dancing(line):
    split = line.split(" ")
    n = int(split[0])
    surprises = int(split[1])
    p = int(split[2])
    scores = []
    for score in split[3:]:
        scores.append(int(score))
    scores.sort(reverse=True)

    s = 0
    ret = 0
    for score in scores:
        high = (score + 2) / 3
        if high >= p:
            ret += 1
            continue

        # max number only increases if score % 3 == {0,2}
        if score % 3 != 1:
            high += 1

        if score > 1 and score < 29 and high >= p and s < surprises:
            ret += 1
            s += 1

    return ret

if __name__ == '__main__':
	main()
