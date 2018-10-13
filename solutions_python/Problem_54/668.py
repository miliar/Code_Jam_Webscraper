"""They happened 26000, 11000 and 6000 slarboseconds ago
Working backwards, 6000 ago they were 20000, 5000, and 0 ago.
Right, so GCF is 5000!  We're getting there!
Starting with smallest, 6000, when's next multiple of 5000?  In 4000,
which works for others too, and is answer.
"""
# Google Code Jam 2010.
# Larry Engholm, 5/7/2010

# Problem description:
# http://code.google.com/codejam/contest/dashboard?c=433101#s=p1
import fractions
def test(times):
    gcd = reduce(fractions.gcd,[t-min(times) for t in times])
    # e.g., 5000
    y = gcd-min(times)          # e.g., -1000
    while y < 0:
        y += gcd                # e.g., 4000
    while 1:
        newtimes = [t + y for t in times]
        if min([t % gcd for t in newtimes]) == 0: return y
        y += gcd

def main():
    file = open('c:/Documents and Settings/Larry/My Documents/Downloads/B-small-attempt0.in')
    numLines = int(file.readline())
    for i in range(numLines):
        times = map(int, file.readline().split()[1:])
        print 'Case #{0}: {1}'.format(i+1, test(times))
main()
