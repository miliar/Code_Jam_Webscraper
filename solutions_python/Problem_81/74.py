from functools import *


class Records (list):
    
    def getOpponents (self, team):
        opponents = []
        for o in range(len(self[team])):
            if   self[team][o] == "0": opponents.append(o)
            elif self[team][o] == "1": opponents.append(o)
        return opponents

    def getWP (self, team, exclude=-1):
        wins = 0
        losses = 0
        for i in range(len(self[team])):
            if i == exclude: continue
            r = self[team][i]
            if   r == "0": losses += 1
            elif r == "1": wins   += 1
        return float(wins) / float(wins+losses)
    
    def getOWP (self, team):
        opponents = self.getOpponents(team)
        return sum(map(partial(self.getWP, exclude=team), opponents)) / float(len(opponents))
    
    def getOOWP (self, team):
        opponents = self.getOpponents(team)
        return sum(map(self.getOWP, opponents)) / float(len(opponents))
    
    def getRPI (self, team):
        wp   = self.getWP(team)
        owp  = self.getOWP(team)
        oowp = self.getOOWP(team)
        return 0.25*wp + 0.5*owp + 0.25*oowp


def main ():
    
    input = open("input.txt")
    testcases = int(input.readline())
    
    case = 1
    while True:
        
        line = input.readline().strip()
        if line == "": break
        teams = int(line)
        
        records = Records([None for i in range(teams)])
        global gRecords
        gRecords = records
        for i in range(teams):
            line = input.readline()
            records[i] = [c for c in line]
    
        scores = map(records.getRPI, range(teams))
        print "Case #%d:" % case
        for score in scores: print score
        case += 1


if __name__ == "__main__": main()