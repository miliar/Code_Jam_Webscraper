#!/usr/bin/env python

import sys

scores = []
wps = []
owps = []
oowps = []
rips = []

def print_scores():
    for line in scores:
        print line

def print_wps():
    print wps

def print_owps():
    print owps

def print_oowps():
    print oowps

def print_rips():
    print rips

def compute_wps():
    for team, line in enumerate(scores):
        sum = 0.0
        n_terms = 0.0
        for res in line:
            if res != -1:
                sum += res
                n_terms += 1.0
        wps.append(sum/n_terms)

def compute_owps():
    for team, line in enumerate(scores):
        sum = 0.0
        n   = 0.0
        for other_team_th, other_team in enumerate(scores):
            if scores[team][other_team_th] == -1:
                #print "Team", team, "skips team", other_team_th
                continue
            if other_team_th == team:
                continue
            other_team_wp = 0.0
            n_terms = 0.0
            for resth, res in enumerate(other_team):
                if res != -1 and resth != team:
                    other_team_wp += res
                    n_terms += 1.0

            sum += other_team_wp/n_terms
            n   += 1.0

        owps.append(sum/n)

def compute_oowps():
    for team_th, team in enumerate(scores):
        sum = 0.0
        n_terms = 0.0
        for i, score in enumerate(scores[team_th]):
            if score == -1:
                continue
            sum += owps[i]
            n_terms += 1.0

        oowps.append(sum/n_terms)

def compute_rips():
    for i in range(len(scores)):
        rips.append(0.25 * wps[i] + 0.5 * owps[i] + 0.25 * oowps[i])
        
def add_line(l, s):
    for c in s:
        if c == '.':
            l.append(-1)
        elif c.isdigit():
            l.append(int(c))
        else:
            return

if __name__ == '__main__':
    data = sys.stdin.readlines()
    n_tests = int(data.pop(0))
    #print "running ", n_tests, " tests "
    for i in range(1, n_tests+1):
        scores = []
        wps = []
        owps = []
        oowps = []
        rips = []
        n_teams = int(data.pop(0)[:-1])
        #print "There are ", n_teams, " teams"
        for team in range(n_teams):
            #scores.append(data.pop(0))
            scores.append([])
            add_line(scores[team], data.pop(0))
            
        #print_scores()

        compute_wps()
        #print_wps()

        compute_owps()
        #print_owps()

        compute_oowps()
        #print_oowps()

        compute_rips()
        #print_rips()
        print "Case #" + str(i) + ":"
        for r in rips:
            print r
