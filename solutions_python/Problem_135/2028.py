# -*- coding: utf-8 -*-

def getSet():
    r = int(raw_input())
    s = set()
    for i in xrange(1,5):
        l = raw_input()
        if i == r:
            s.update([int(t) for t in l.split()])
    return s
	

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        s = getSet() & getSet()
        ans = 'Bad magician!'
        if len(s) == 0:
            ans = 'Volunteer cheated!'
        elif len(s) == 1:
            ans = str(s.pop())
        print("Case #%i: %s" % (caseNr, ans))

