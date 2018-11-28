#!/bin/env python
import sys

n_case = int(sys.stdin.readline())

for ix_case in range(n_case):
   n_team = int(sys.stdin.readline())
   map_team = []
   wp_team = []
   owp_wp_team = []
   owp_team = []
   oowp_team = []
   rip_team = []
   for ix_team in range(n_team):
      map_team.append(sys.stdin.readline().rstrip())
   # calculate wp
   for ix_team in range(n_team):
      tmp_wp = []
      win = map_team[ix_team].count('1')
      lose = map_team[ix_team].count('0')
      total = float(win+lose)
      wp_team.append(win/total)
      for ix2_team in range(n_team):
         if map_team[ix_team][ix2_team] is '1':
            tmp_wp.append((win-1)/(total-1))
         elif map_team[ix_team][ix2_team] is '0':
            tmp_wp.append((win)/(total-1))
         else:
            tmp_wp.append(wp_team[ix_team])
      owp_wp_team.append(tmp_wp)
   # calculate owp
   for ix_team in range(n_team):
      n_opp = 0
      score_opp = 0
      for ix_opp in range(n_team):
         if map_team[ix_team][ix_opp] is not '.' and ix_team is not ix_opp:
            n_opp += 1
            score_opp += owp_wp_team[ix_opp][ix_team]
      owp_team.append(score_opp/n_opp)
   # calculate oowp
   for ix_team in range(n_team):
      n_opp = 0
      score_opp = 0
      for ix_opp in range(n_team):
         if map_team[ix_team][ix_opp] is not '.':
            n_opp += 1
            score_opp += owp_team[ix_opp]
      oowp_team.append(score_opp/n_opp)
   # calculate rip
   for ix_team in range(n_team):
      rip_team.append(0.25 * wp_team[ix_team] + 0.5 * owp_team[ix_team] + 0.25 * oowp_team[ix_team])
   print('Case #%d:' % (ix_case+1))
   print('\n'.join([str(e) for e in rip_team]))
