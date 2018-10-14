#!/usr/bin/env python
import sys
import re
"""
2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.

Case #1:
0.5
0.5
0.5
Case #2:
0.645833333333
0.368055555556
0.604166666667
0.395833333333
"""
class TestCase:
    N_pattern = re.compile(r'^\s*(\d+)')

    def execute(self):
        #print('teams: ' + str(self.teams))
        #RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        WPs = []
        OWPs = []
        RPIs = []
        k = 0
        for team in self.teams:
            n_matches = sum([1 for x in team if x == '0' or x == '1'])
            #print('n_matches: ' + str(n_matches))
            n_win = sum([1 for x in team if x == '1'])
            #print('n_win: ' + str(n_win))
            WP = n_win / n_matches
            WPs.append(WP)
            #print('WP: ' + str(WP))
            opponents = [i for i in range(self.N) if team[i] == '0' or team[i] == '1']
            #print('opponents: ' + str(opponents))
            OWP = 0
            for i in opponents:
                n_opp_matches = sum([1 for x in range(self.N) if (self.teams[i][x] == '0' or self.teams[i][x] == '1') and (x != k)])
                #print(str(i) + '. n_opp_matches: ' + str(n_opp_matches))
                n_opp_win = sum([1 for x in range(self.N) if (self.teams[i][x] == '1') and (x != k)])
                #print(str(i) + '. n_opp_win: ' + str(n_opp_win))
                #print('OWP ' + str(i) + ': ' + str(n_opp_win / self.N))
                OWP += n_opp_win / n_opp_matches
                #OWP += n_opp_win / self.N
            OWP = OWP / len(opponents)
            #print('OWP: ' + str(OWP))
            OWPs.append(OWP)
            #OOWP = OWP / len(opponents)
            #print('OOWP: ' + str(OOWP))
            #RPIs.append("%0.12f" % (0.25 * WP + 0.5 * OWP + 0.25 * OOWP))
            k += 1

        k = 0
        for team in self.teams:
            opponents = [i for i in range(self.N) if team[i] == '0' or team[i] == '1']
            #print('opponents: ' + str(opponents))
            OOWP = 0
            for i in opponents:
                OOWP += OWPs[i]
            OOWP = OOWP / len(opponents)
            #print('OOWP: ' + str(OOWP))
            RPIs.append("%0.12f" % (0.25 * WPs[k] + 0.5 * OWPs[k] + 0.25 * OOWP))
            k += 1
        return '\n'.join(RPIs)

    def __init__(self, case_number, f):
        input_line = f.readline()
        match = TestCase.N_pattern.search(input_line)
        self.N = int(match.group(1))

        self.teams = []
        for i in range(self.N):
            self.teams.append(f.readline().strip())

        print('Case #' + str(case_number) + ":\n" + self.execute())

n_test_cases = int(sys.stdin.readline())
for i in range(n_test_cases):
    TestCase(i+1, sys.stdin)

