#!/usr/bin/env python
import sys
import psycho

class InputException(Exception):
    pass

def parse_file(filename):
    f = file(filename, 'r')
    case_num = int(f.readline())
    lines = f.readlines()
#    if len(lines) != case_num:
#        raise InputException("bad input: case number mismatch")
    f.close()
    cases = []
    i = 0
    while i < len(lines):
        n = int(lines[i])
        i+=1
        schedules = []
        for j in xrange(n):            
            schedules.append(lines[i].strip())
            i += 1
        
        cases.append((n, schedules))
        
    return cases

def rpi(schedules, team):    
    return 0.25 * wp(schedules[team], None) + 0.5 * owp(schedules, team) + 0.25 * oowp(schedules, team)

def wp(schedule, null_game):
    games = 0.
    wins = 0.
    for i in xrange(len(schedule)):
        if i == null_game or schedule[i] == '.':
            continue
        games += 1
        if schedule[i] == '1':
            wins += 1
    return wins / games

def owp(schedules, team):
    if len(schedules) == 1:
        return 1. 
    
    total = 0.
    opponents = 0
    for op in xrange(len(schedules)):
        if op == team or schedules[team][op] == '.':
            continue
        opponents += 1
#        op_sched = schedules[op]
#        op_sched = op_sched[:team] + '.' + op_sched[team +1 :]
        total += wp(schedules[op], team)
    
    if opponents == 0:
        return 0
    return total / opponents

def oowp(schedules, team):
    total = 0. 
    opponents = 0
    for op in xrange(len(schedules)):
        if team == op or schedules[team][op] == '.':
            continue
        total += owp(schedules, op)
        opponents += 1
    if opponents == 0:
        return 0
    
    return total / opponents

def solve_case(n, schedules):
    return [rpi(schedules, i) for i in xrange(n)]

def main():
    if len(sys.argv) != 3:
        print 'usage: %s <inputfile> <outputfile>' % sys.argv[0]
        return
    
    try:
        cases = parse_file(sys.argv[1])
    except InputException, e:
        print 'Got exception:', e
        return
    
    sys.stdout = file(sys.argv[2], 'w')
    
    for count in xrange(len(cases)):                   
        print 'Case #%d:' % (count + 1)
        rpis = solve_case(*cases[count])
        for rpi in rpis:
            print rpi
         
if __name__=='__main__':
    main()
