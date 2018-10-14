import sys
# no surprise: 3 * personalBest - 2 = total
# surprise: 3 * personalBest - 4 = total
def decision(bestResult, surprising, totals):
    # if bestResult / 3
    definite = 0
    onlySurprise = 0
    nos = 0
    for t in totals:
        if 3 * bestResult - 2 <= t:
            definite += 1
        elif 3 * bestResult - 4 <= t and t >= bestResult:
            onlySurprise += 1
    return definite + min(onlySurprise, surprising)




def main(fName):
    f = open(fName, "r")
    cases = int(f.readline())
    for i in xrange(cases):
        caseNo = i + 1
        nums = map(int, f.readline().split())
        googlers = nums[0]
        surprising = nums[1]
        p = nums[2]
        totals = nums[3:]
        print "Case #%d: %d" % (caseNo, decision(p, surprising, totals))

main(sys.argv[1])
