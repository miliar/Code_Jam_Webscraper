import sys, unittest

def countChar(s, c):
    count = 0
    for char in s:
        if char in c:
            count += 1
    return count

WP_memo = {}

def calcWP(data):
    if data in WP_memo:
        return WP_memo[data]
    total = countChar(data, '10')
    if total == 0:
        return 0
    wp = countChar(data, '1') / float(total)
    WP_memo[data] = wp
    return wp

def isOpponent(char):
    return char == '1' or char == '0'

def prefix(data, teams):
    if teams == 0:
        return ''
    return data[:teams]

def suffix(data, teams):
    if teams == len(data):
        return ''
    return data[(teams+1):]

def without(data, teams):
    return prefix(data, teams) + '.' + suffix(data, teams)

def calcOWP(teamData, teams):
    count = 0
    sum = 0
    data = teamData[teams]
    for i in range(0, len(data)):
        if isOpponent(data[i]):
            count += 1
            sum += calcWP(without(teamData[i], teams))
    return sum / float(count)

def calcOOWP(teamsData, teams):
    count = 0
    sum = 0
    data = teamsData[teams]
    for i in range(0, len(data)):
        if isOpponent(data[i]):
            count += 1
            sum += calcOWP(teamsData, i)
    return sum / float(count)

def calcRPI(teamsData, team):
    return 0.25 * calcWP(teamsData[team]) + 0.5 * calcOWP(teamsData, team) + 0.25 * calcOOWP(teamsData, team)

def eatData(lines, N):
    result = []
    for i in range(0, N):
        result.append(lines.pop(0))
    return result

def main():
    lines = [line.rstrip() for line in open(sys.argv[1])]
    lines.pop(0)
    count = 1
    while len(lines) != 0:
        N = int(lines.pop(0))
        teamData = eatData(lines, N)
        print 'Case #%d:' % count
        for i in range(0, N):
            print calcRPI(teamData, i)
        count += 1
        

class Test(unittest.TestCase):
    def setUp(self):
        self.teamData = [ '.11.','0.00','01.1','.10.' ]

    def testWithout(self):
        self.assertEqual( '.1', prefix('.11.', 2) )
        self.assertEqual( '.1..', without('.11.', 2))
        self.assertEqual( '10..', without('10.1', 3))

    def testCalcWP(self):
        self.assertEqual( 1, calcWP( '.11.' ) )
        self.assertEqual( 2/float(3), calcWP( '01.1' ) )
        self.assertEqual( 0, calcWP( '....' ) )

    def testCalcOWP(self):
        self.assertEqual( 0.25, calcOWP( self.teamData, 3 ) )

    def testCalcOOWP(self):
        self.assertAlmostEqual( 7/float(12), calcOOWP( self.teamData, 0) )

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        unittest.main()
