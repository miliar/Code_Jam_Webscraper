# -*- coding: utf-8 -*-

import unittest
import sys


def calculate_rpi(grid):
    # wp
    wps = []
    owps = []
    for i in range(len(grid)):
        wins = 0
        total_matches = len(grid[i])
        for match in grid[i]:
            if match == '.':
                total_matches -= 1
            elif match == '1':
                wins += 1
        wps.append(wins / float(total_matches))

        sumowps = 0
        opponents = len(grid)
        for j in range(len(grid)):
            if i == j or grid[i][j] == '.':
                opponents -= 1
                continue
            wins = 0
            total_matches = len(grid[j])
            for h in range(len(grid[j])):
                if h == i:
                    total_matches -= 1
                elif grid[j][h] == '.':
                    total_matches -= 1
                elif grid[j][h] == '1':
                    wins += 1
            print i, j, wins, total_matches
            sumowps += wins / float(total_matches)
        owps.append(sumowps / float(opponents))

    print wps
    print owps

    # oowp
    oowps = []
    for i in range(len(owps)):
        oowpsum = 0
        opponents = 0
        for j in range(len(owps)):
            if j != i and grid[i][j] != '.':
                oowpsum += owps[j]
                opponents += 1
        oowps.append(oowpsum / float(opponents))

    print oowps

    # rpi
    rpis = []
    for i in range(len(wps)):
        rpis.append(0.25 * wps[i] + 0.50 * owps[i] + 0.25 * oowps[i])

    return rpis


class RpiTest(unittest.TestCase):

    def test_basic(self):

        grid = ['.10', '0.1', '10.']
        self.assertEqual(calculate_rpi(grid),
                         [0.5, 0.5, 0.5])

        grid = ['.11.',
                '0.00',
                '01.1',
                '.10.']
        self.assertEqual(calculate_rpi(grid),
                         [0.645833333333,
                          0.368055555556,
                          0.604166666667,
                          0.395833333333,
                          ])


def main():
    fin = open(sys.argv[1])
    fout = open(sys.argv[2], 'w')

    t = int(fin.readline().strip())

    for case in range(t):
        n = int(fin.readline().strip())
        grid = []
        for teams in range(n):
            grid.append(fin.readline().strip())
        rpis = calculate_rpi(grid)
        fout.write('Case #%d:\n' % (case + 1))
        fout.write('\n'.join([str(rpi) for rpi in rpis]) + '\n')

    fout.close()
    fin.close()


if __name__ == '__main__':
    main()
