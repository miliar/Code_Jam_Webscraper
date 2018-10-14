#!/usr/bin/env python2.7

from collections import defaultdict

WIN="1"
LOSS="0"
NPL="."

T = int(raw_input())

for case in range(T):
  N = int(raw_input())
  results = {} # (team1, team2) -> result
  games = defaultdict(int) # team -> games
  wins = defaultdict(int) # team -> wins
  games_excl = defaultdict(int) # (team, other) -> games excluding other
  wins_excl = defaultdict(int) # (team, other) -> wins excluding other

  for team1 in range(N):
    team_results = raw_input()

    for team2 in range(N):
      result = team_results[team2]

      if result != ".":
        results[team1, team2] = result
        games[team1] += 1

        if result == WIN:
          wins[team1] += 1

        for other in range(N):
          if other != team1 and other != team2:
            games_excl[team1, other] += 1

            if result == WIN:
              wins_excl[team1, other] += 1

  WP = {}
  OWP = {}

  for team1 in range(N):
    WP[team1] = float(wins[team1]) / games[team1]
    OWPs = [float(wins_excl[team2, team1]) / games_excl[team2, team1]
               for team2 in range(N) if team2 != team1
                                       and (team1, team2) in results]
    OWP[team1] = sum(OWPs) / len(OWPs)

  print "Case #%d:" % (case+1)

  for team1 in range(N):
    OWPs = [OWP[team2] for team2 in range(N) if team2 != team1
                                      and (team1, team2) in results]
    OOWP = sum(OWPs) / len(OWPs)
    print 0.25 * WP[team1] + 0.50 * OWP[team1] + 0.25 * OOWP
