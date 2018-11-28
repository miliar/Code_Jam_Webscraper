#!/usr/bin/python2
import sys

class Team(object):
    def __init__(self, idx):
        self.idx = idx
        self.games = []

    def __str__(self):
        return 'Team %d' % self.idx

    def opponents(self):
        return map(lambda (team, result): team, self.games)

    def lost_games(self):
        return filter(lambda (team, result): not result, self.games)

    def won_games(self, ex=None):
        return filter(lambda (team, result): result and team != ex, self.games)

    def all_games(self, ex=None):
        return filter(lambda (team, result): team != ex, self.games)

    def rpi(self):
        return .25 * self.wp() + 0.5 * self.owp() + .25 * self.oowp()

    def wp(self, r=None):
        return float(len(self.won_games(r))) / len(self.all_games(r))

    def owp(self, r=None):
        opponents = self.opponents()
        #if r: opponents.remove(r)
        return float(sum(map(lambda t: t.wp(self), opponents))) / len(opponents)

    def oowp(self):
        opponents = self.opponents()
        return float(sum(map(lambda t: t.owp(self), opponents))) / len(opponents)

    def win(self, other):
        self.games.append((other, True))

    def lose(self, other):
        self.games.append((other, False))

if len(sys.argv) < 2:
    print 'Usage: %s <input file>' % sys.argv[0]
    sys.exit(1)

fp = open(sys.argv[1])
cases = int(fp.readline())

i = 1

for i in xrange(cases):
    numteams = int(fp.readline())
    teams = []

    # Add all teams
    map(lambda x: teams.append(Team(x)), xrange(numteams))

    for t in xrange(numteams):
        team = teams[t]
        
        data = fp.readline().strip()
        for j in xrange(len(data)):
            other = teams[j]

            if data[j] == '1':
                #print team, 'won from', other
                team.win(other)
            elif data[j] == '0':
                #print team, 'lost to', other
                team.lose(other)
            else:
                pass
                #print team, 'ignore'
             
        

    print 'Case #%d:' % (i+1)
    for team in teams:
        print team.rpi()

