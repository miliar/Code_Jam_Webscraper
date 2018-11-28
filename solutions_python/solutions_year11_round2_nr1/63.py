import sys

def calc_games_won(team):
  # returns nom/denom tuple
  return (len(filter(lambda x: x == "1", team)), 
          len(filter(lambda x: x == "1" or x == "0", team)))

def to_frac(tup):
  return 1.0 * tup[0] / tup[1]

def excl(tup, result):
  #THIS might be a off a bit
  return to_frac((tup[0] - (0 if result == "1" else 1), tup[1] - 1))

def calc_owp(team, wp):
  # get all teams you played against
  teams_against = filter(lambda x: x[1] != ".", enumerate(team))
  # get their WP w/ yours excluded
  average = sum([excl(wp[t], r) for t,r in teams_against])/len(teams_against)
  return average

def calc_oowp(team, owp):
  teams_against = filter(lambda x: x[1] != ".", enumerate(team))
  average = sum([owp[t] for t,r in teams_against]) / len(teams_against)
  return average

def solve_case(input_f):
  num_teams = int(input_f.readline().strip())
  team_matrix = list(range(num_teams))
  for x in xrange(num_teams):
    team_matrix[x] = list(input_f.readline().strip())

  wp = [calc_games_won(team) for team in team_matrix] #stored as nom/denom
  owp = [calc_owp(team, wp) for team in team_matrix] 
  oowp = [calc_oowp(team, owp) for team in team_matrix]
  
  for x in range(num_teams):
    print "%.12F" % (.25 * to_frac(wp[x]) + .5 * owp[x] + .25 * oowp[x],)

#main
input_f = open(sys.argv[1])
num_cases = int(input_f.readline())
for c in xrange(1, num_cases+1):
  print "Case #%d:" % (c,)
  solve_case(input_f)
