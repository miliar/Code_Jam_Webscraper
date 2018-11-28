from codecs import open as cOpen
from sys import argv, stderr

BASERATE = 2.0

def timeToReachGoal(goal, rate, farms):
    return goal / (2 + (rate * farms))

def runSim(farmCost, rateChange, goal, farms=0, time=0):
    sQuoTime = time + timeToReachGoal(goal, rateChange, farms)
    nextFarmTime = timeToReachGoal(farmCost, rateChange, farms)
    newFarmTime = time + nextFarmTime + timeToReachGoal(goal, rateChange, farms +1)
    # the comparison is myopic, but we are dealing with two linear lines so it's fairly unimportant here
    while newFarmTime < sQuoTime:
        farms += 1
        time += nextFarmTime
        sQuoTime = time + timeToReachGoal(goal, rateChange, farms)
        nextFarmTime = timeToReachGoal(farmCost, rateChange, farms)
        newFarmTime = time + nextFarmTime + timeToReachGoal(goal, rateChange, farms +1)
    return sQuoTime
    


def main(f):
    caseResults = []
    with cOpen(f, encoding ='utf-8-sig') as input:
        cases = int(input.next().strip())
        for i in xrange(1, cases + 1):
            farmCost, rateChange, goal = [float(f) for f in input.next().split(' ')]
            caseResults.append('Case #' + str(i) + ': %s'  % round(runSim(farmCost, rateChange, goal, farms=0), 7))
    return caseResults

testGoals = ['Case #1: 1.0',
    'Case #2: 39.1666667',
    'Case #3: 63.9680013',
    'Case #4: 526.1904762']

if __name__ == '__main__':
    testResults = main('cookie_sample.txt')
    for i, result in enumerate(testResults):
        try:
            assert result == testGoals[i]
        except AssertionError:
            stderr.write('Case %s Incorrect\n' %i)
            stderr.write('Expected:%s\n' % testGoals[i].split(' ')[-1])
            stderr.write('Got:%s\n' % result.split(' ')[-1])
    if len(argv) > 1:
        for line in main(argv[1]):
            print line