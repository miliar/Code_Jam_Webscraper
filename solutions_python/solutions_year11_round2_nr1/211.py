#!/usr/bin/python
#coding:utf8

#RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
class Team(object):
    def __init__(self):
        self.games = 0
        self.victories = 0
        self.other_games = 0
        self.owp = 0 
        self.other_players = 0
        self.opponents = [] 
    def wp(self):
        return 1.0 * self.victories / self.games
    def oowp(self, teams):
        saida  = 0
        for i in self.opponents:
            saida += teams[i].owp
        saida /= len(self.opponents)
        return saida

def game_on(score):
    #print "*"* 10
    #print score
    teams = []
    for i in range(len(score)):
        scr = score[i]
        t = Team()
        t.victories = scr.count("1")
        t.games = scr.count("1") + scr.count("0")
        others = score[:i] + score[i+1:]
        for other in others:
            if other[i] != ".":
                other = other[:i] + other[i+1:]
                t.owp += 1.0 * other.count("1") / (other.count("1") + other.count("0"))
                t.other_players += 1
        t.owp /= t.other_players
        for pos, l in enumerate(scr):
            if l in ['1','0']:
                t.opponents.append(pos)
        teams.append(t)
    for t in teams:
        #print "WP", t.wp(), "OWP", t.owp , "oowp", t.oowp(teams)
        rpi = 0.25 * t.wp() + 0.50 * t.owp + 0.25 * t.oowp(teams)
        print rpi

if __name__ == '__main__':
    num = input()
    for i in range(num):
        tmp = input()
        teams = []
        for j in range(tmp):
            case = raw_input().strip()
            teams.append(case)
        print "Case #%s:"% (i+1)
        game_on(teams)
