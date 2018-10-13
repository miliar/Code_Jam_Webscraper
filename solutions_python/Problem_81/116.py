#! /usr/bin/python
# GCJ 2011 R1B - RPI

from sys import stdin


def read_test_case(input_data) :
    team_count = int(input_data.pop(0))
    team_data = [input_data.pop(0).strip() for i in range(team_count)]
    return (team_count, team_data)


def calc_wp(team_count, team_data) :
    wp = []
    for i in range(team_count) :
        games_played, games_won = 0, 0
        for j in range(team_count) :
            if team_data[i][j] != '.' :
                games_played += 1
                if team_data[i][j] == '1' :
                    games_won += 1
        wp.append(float(games_won) / games_played)
    return wp


def calc_owp(team_count, team_data) :
    owp = []
    for i in range(team_count) :
        teams_played_against, op_wp_sum = 0, 0.0
        for j in range(team_count) :
            if team_data[i][j] != '.' :
                op_played, op_won = 0, 0
                for k in range(team_count) :
                    if k != i and team_data[j][k] != '.' :
                        op_played += 1
                        if team_data[j][k] == '1' :
                            op_won += 1
                teams_played_against += 1
                op_wp_sum += (float(op_won) / op_played)
        owp.append(op_wp_sum / teams_played_against)
    return owp


def calc_oowp(team_count, team_data, owp) :
    oowp = []
    for i in range(team_count) :
        games_played, owp_sum = 0, 0.0
        for j in range(team_count) :
            if team_data[i][j] != '.' :
                games_played += 1
                owp_sum += owp[j]
        oowp.append(owp_sum / games_played)
    return oowp


def calc_rpi(wp, owp, oowp) :
    rpi = []
    for (w, ow, oow) in zip(wp, owp, oowp) :
        rpi.append(w * 0.25 + ow * 0.5 + oow * 0.25)
    return rpi


def print_solution(test_case_id, rpi) :
    print('Case #{0}:'.format(test_case_id))
    for x in rpi :
        print(x)


def main() :
    input_data = stdin.readlines()
    test_count = int(input_data.pop(0))

    for i in range(1, test_count+1) :
        team_count, team_data = read_test_case(input_data)
        wp = calc_wp(team_count, team_data)
        owp = calc_owp(team_count, team_data)
        oowp = calc_oowp(team_count, team_data, owp)
        rpi = calc_rpi(wp, owp, oowp)
        print_solution(i, rpi)

if __name__ == '__main__' :
    main()
