import sys

def solve(testCaseNumber):
    line = raw_input().strip()
    strSmax, shyness = line.split()
    Smax = int(strSmax)
    shyness = map(int, shyness.strip())
    required, total = 0, 0
    for i in xrange(len(shyness)):
        if total < i:
            required += i-total
            total = i
        total += shyness[i]
    print 'Case #{0}: {1}'.format(testCaseNumber, required)


def main():
    T = int(raw_input())
    for i in xrange(1, T+1):
        solve(i)
main()
