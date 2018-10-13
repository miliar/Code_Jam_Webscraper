#Problem D. GoroSort
#Wow. Stupid

from sys import stdin

cases = int(stdin.readline())

##def average(n):
##    #divides the numbers in the wrong place into two piles - twos pile and
##    #threes pile. Since threes piles takes less time to sort
##    #it greedily assigns most of the work to it
####    def threes(n):
####        if n % 3 == 1: return (n-4)/3
####        return n/3
##    prob2 = 2.0
##    prob3 = 3.49982218158
####    th = threes(n)
####    tw = (n - th*3)/2
##    if n % 2 == 0:
##        tw, th = n / 2, 0
##    else:
##        tw, th = n / 2 - 1, 1
####    print '\ntotal wrong: %d\tthrees: %d\ttwos: %d\n' % (n, th, tw)
##    return tw * prob2 + th * prob3
    

for caseNo in xrange(1, cases+1):
    piles = int(stdin.readline())
    pile = [int(x) for x in stdin.readline().split()]
    missing = 0
    for i, no in enumerate(pile):
        if no != i + 1:
            missing += 1
##    result = average(missing)
    print "Case #%d: %.6f" % (caseNo, missing)
