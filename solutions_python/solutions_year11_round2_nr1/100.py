from fractions import gcd
from math import ceil
from math import floor

def calc_rpi(schedule):
    games = {}
    num_teams = len(schedule)
    for first_index in range(num_teams - 1):
        for second_index in range(first_index + 1, num_teams):
            matchup = schedule[first_index][second_index]
            if matchup != '.':
                if first_index not in games:
                    games[first_index] = {'opp_w': [],
                                          'opp_l': [],
                                          'games': 0,
                                          'wins': 0}
                if second_index not in games:
                    games[second_index] = {'opp_w': [],
                                           'opp_l': [],
                                           'games': 0,
                                           'wins': 0}

                games[first_index]['games'] += 1
                games[second_index]['games'] += 1
                if matchup == '1':
                    games[first_index]['wins'] += 1
                    games[first_index]['opp_w'].append(second_index)
                    games[second_index]['opp_l'].append(first_index)
                elif matchup == '0':
                    games[second_index]['wins'] += 1
                    games[first_index]['opp_l'].append(second_index)
                    games[second_index]['opp_w'].append(first_index)
                else:
                    raise Exception("Bad")

    for team in games:
        owp_sum = 0
        total = 0
        for opp in games[team]['opp_w']:
            owp_sum += 1.0*games[opp]['wins']/(games[opp]['games'] - 1)
            total += 1
        for opp in games[team]['opp_l']:
            owp_sum += 1.0*(games[opp]['wins'] - 1)/(games[opp]['games'] - 1)
            total += 1
        games[team]['owp'] = (owp_sum*1.0)/total

    for team in games:
        oowp_sum = 0
        total = 0
        for opp in games[team]['opp_w']:
            oowp_sum += games[opp]['owp']
            total += 1
        for opp in games[team]['opp_l']:
            oowp_sum += games[opp]['owp']
            total += 1
        games[team]['oowp'] = (oowp_sum*1.0)/total

    result = []
    for i in range(num_teams):
        rpi = sum([(0.25*games[i]['wins'])/games[i]['games'],
                   0.5*games[i]['owp'],
                   0.25*games[i]['oowp']])
        result.append(rpi)
    return result

# Each 1 in a team's row represents a win, and each 0 represents a loss.
# If the schedule contains a '1' in row i, column j,
# then it contains a '0' in row j, column i.
# If the schedule contains a '0' in row i, column j,
# then it contains a '1' in row j, column i.

with open('A-large.in', 'r') as fh:
    data = [row for row in fh.read().split('\n') if row]

num_cases = int(data[0])

result = ''
index = 1
for case in range(1, num_cases + 1):
    num_players = int(data[index])
    rpi_vals = calc_rpi(data[index + 1:index + num_players + 1])
    to_print = ["Case #%s:" % case] + [str(val) for val in rpi_vals]
    to_print = '\n'.join(to_print)
    print to_print
    index += 1 + num_players
    result += to_print + '\n'

with open('A-large.out', 'w') as fh:
    fh.write(result)
