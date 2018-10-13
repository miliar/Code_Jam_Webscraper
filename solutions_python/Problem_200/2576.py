import sys

def isTidy(n):
    s = str(n)
    prevDigit = '0'
    for digit in s:
        if digit < prevDigit:
            return False
        prevDigit = digit
    return True

caseNum = -1
for line in sys.stdin:
    caseNum += 1
    if caseNum == 0:
        continue
    n = int(line)
    ans = 1
    for i in range(2, n + 1):
        if isTidy(i):
            ans = i
    print "Case #" + str(caseNum) + ":", ans
