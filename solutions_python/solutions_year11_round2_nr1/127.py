#!/usr/bin/env python
import sys

def WP(s, t):
    won = 0
    total = 0
    for c in s[t]:
        if c == '1':
            won += 1
            total += 1
        if c == '0':
            total += 1
    return float(won) / total

memoized_owp = {}
def OWP(s, t):
    if (s, t) in memoized_owp:
        return memoized_owp[(s, t)]
    grand_total = 0
    grand_divisor = 0
    for opponent_i in range(len(s)):
        if opponent_i == t:
            continue # its us
        if s[t][opponent_i] == '.':
            continue # we didn't face them
        opponent_total = 0
        opponent_divisor = 0
        for game_i in range(len(s)):
            if game_i == t:
                continue # game against us
            if s[opponent_i][game_i] == '1':
                opponent_total += 1
                opponent_divisor += 1
            if s[opponent_i][game_i] == '0':
                opponent_divisor += 1
        grand_total += float(opponent_total) / opponent_divisor
        grand_divisor += 1
    memoized_owp[(s,t)] = grand_total / grand_divisor
    return grand_total / grand_divisor # grand average

def OOWP(s, t):
    total = 0
    divisor = 0
    for opponent_i in range(len(s)):
        if opponent_i == t:
            continue # its us
        if s[t][opponent_i] == '.':
            continue # we didn't face them
        total += OWP(s, opponent_i)
        divisor +=1
    return float(total) / divisor

T = int(sys.stdin.readline())
for j in range(T):
    line = sys.stdin.readline().rstrip()
    N = int(line)
    s = []
    for n in range(N):
        s.append(sys.stdin.readline().rstrip())

    print "Case #%d:" % (j + 1)
    for i in range(N):
        #print "WP:", WP(s, i)
        #print "OWP:", OWP(s, i)
        #print "OOWP:", OOWP(s, i)
        RPI = 0.25 * WP(s, i) + 0.50 * OWP(s, i) + 0.25 * OOWP(s, i)
        print RPI
