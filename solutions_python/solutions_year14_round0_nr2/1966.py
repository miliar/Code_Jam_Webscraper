# -*- coding: utf-8 -*-


def solve(C,F,X):
    s = 0.0
    rate = 2.0
    while True:
        ds = C / rate
        if X / (rate + F) + ds < X / rate:
            s = s + ds
            rate = rate + F
        else:
            return s + X / rate
	

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        [C,F,X] = [float(t) for t in raw_input().split()]
        ans = str(solve(C,F,X))
        print("Case #%i: %s" % (caseNr, ans))

