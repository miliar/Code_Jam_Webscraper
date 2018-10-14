#!/usr/bin/python

if __name__ == "__main__":
    T = int(raw_input())  # T is the number of Test Cases
    for i in xrange(T):
        tp = tuple(map(int, raw_input().split()))
        N = tp[0]
        S = tp[1]
        p = tp[2]

        b1 = 3 * p - 2  # boundary 1
        b1 = 0 if b1 < 0 else b1
        b2 = 3 * p - 5  # boundary 2
        b2 = 0 if b2 < 0 else b2
        c1 = c2 = c3 = 0
        for j in xrange(3,N+3):
            if tp[j] >= b1:
                c1 += 1
            elif b1 > tp[j] > b2:
                c2 += 1
            else:
                c3 += 1
        if S >= c2:
            ans = c1 + c2
        else:
            ans = c1 + S
        print "Case #" + str(i+1) + ": " + str(ans)
    
