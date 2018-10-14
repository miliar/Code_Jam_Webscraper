#!/usr/bin/env python


def rpi(matrix):
    n = len(matrix)
    wp = []
    
    # precalculate winning percentage and team plays
    counts = [] # (wins, plays)
    for row in matrix:
        plays = wins = 0
        for c in row:
            if c in '10':
                plays += 1
            if c == '1':
                wins += 1
        assert plays > 0
        counts.append((wins, plays))
        wp.append(float(wins)/plays)

    # calculate owp
    owp = []
    for team, row in enumerate(matrix):
        value = 0.0
        opponents = 0
        for opponent, c in enumerate(row):
            if c != '.':
                opponents += 1
                w, p = counts[opponent]
                # if we lost against them, they won, so subtract
                # always subtract play count
                value += float(w - int(c == '0')) / (p - 1)
        owp.append(value / opponents)

    final = []
    for team, row in enumerate(matrix):
        oowp = 0.0
        opponents = 0
        for opponent, c in enumerate(row):
            if c != '.':
                oowp += owp[opponent]
                opponents += 1
            
        oowp /= opponents

        final.append(0.25 * wp[team] + 0.5 * owp[team] + 0.25 * oowp)

    return final


def main():
    from sys import stdin
    
    ncases = int(stdin.readline())
    for case in range(1, ncases + 1):
        matrix = []
        nteams = int(stdin.readline())
        for row in range(nteams):
            matrix.append(stdin.readline()[:nteams])
        
        print 'Case #%d:' % case
        for value in rpi(matrix):
            print value


if __name__ == '__main__':
    main()
