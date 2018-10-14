#!/usr/bin/python
import sys



if __name__ == "__main__":
    c = int(sys.stdin.readline())
    for cnt in range(1, c+1):
        P,K,L = map(int, sys.stdin.readline().split())
        nums = map(int, sys.stdin.readline().split())
        if P * K < L:
            print "Case %d: Impossible" % (cnt)

        t = zip (nums, range(0, len(nums)))
        t.sort()
        t.reverse()
        keyCount = 1
        remainingKeys = K
        count = 0
        for (num,key) in t:
            count += keyCount * num
            remainingKeys -= 1
            if remainingKeys == 0:
                keyCount += 1 
                remainingKeys = K



        print "Case #%d: %d" % (cnt, count)
