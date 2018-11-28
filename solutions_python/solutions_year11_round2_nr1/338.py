#!/usr/bin/env python

from __future__ import print_function
import sys


def calc_RPI(matrix):
    N = len(matrix)
    WPs = []
    OWPs = []
    OOWPs = []

    for team in matrix:
        team_total = 0
        team_wins = 0
        for game in team:
            if(game == '1'):
                team_wins = team_wins + 1
            if(game != '.'):
                team_total = team_total + 1
        WPs.append(float(team_wins)/float(team_total))

    for i in range(N):
        opponent_WP_total = 0.0
        opponent_WP_num = 0
        for j in range(N):
            if(j != i and matrix[i][j] != '.'):
                opponent_total = 0
                opponent_wins = 0
                for k in range(N):
                    if(k != i):
                        if(matrix[j][k] == '1'):
                            opponent_wins = opponent_wins + 1
                        if(matrix[j][k] != '.'):
                            opponent_total = opponent_total + 1
                opponent_WP = float(opponent_wins)/float(opponent_total)
                # print(i,j,opponent_WP)

                opponent_WP_total = opponent_WP_total + opponent_WP
                opponent_WP_num = opponent_WP_num + 1
        OWPs.append(float(opponent_WP_total)/float(opponent_WP_num))

    for team in matrix:
        OWP_total = 0
        OWP_num = 0
        for i in range(N):
            if(team[i] != '.'):
                OWP_total = OWP_total + OWPs[i]
                OWP_num = OWP_num + 1
        OOWPs.append(float(OWP_total)/float(OWP_num))

    # print(WPs, OWPs, OOWPs)

    RPIs = []
    for i in range(N):
        RPIs.append((0.25*WPs[i]) + (0.50*OWPs[i]) + (0.25*OOWPs[i]))

    # print(RPIs)
    return RPIs


def main(*args):
    if(len(args) < 2):
        print("Usage: %s <input file>" % args[0])

    filename = args[1]
    input_file = open(filename, "rb")
    output_file = open(filename+".out", "wb")

    try:
        input = input_file.readline().strip()
    except:
        print("Premature end of input")

    T = int(input)
    for k in range(T):
        try:
            input = input_file.readline().strip()
        except:
            print("Premature end of input")

        N = int(input)
        teams = []
        for i in range(N):
            input = input_file.readline().strip()
            team = []
            for win_loss in input:
                team.append(win_loss)
            teams.append(team)

        # print (teams)
        RPIs = calc_RPI(teams)
        # print("Case #%d: %d" % (j+1, turns), file=output_file)
        print("Case #%d:" % (k+1), file=output_file)
        for RPI in RPIs:
            print(RPI, file=output_file)

    input_file.close()
    output_file.close()


if(__name__ == "__main__"):
    sys.exit(main(*sys.argv))
