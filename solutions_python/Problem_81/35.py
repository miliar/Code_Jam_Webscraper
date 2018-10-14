#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

filename = sys.argv[1]
f = open(filename, 'r+')

case = int(f.readline())
for c in range(0, case):
  N = int(f.readline().strip())
  teams = []
  for n in range(N):
    board = f.readline()
    win_list = []
    lose_list = []
    for i, ch in enumerate(board):
      if ch == '1':
        win_list.append(i)
      elif ch == '0':
        lose_list.append(i)
    teams.append({'win_list':win_list,
                  'lose_list':lose_list,
                  'win_count':len(win_list),
                  'lose_count':len(lose_list),
                  'WP':None, 'OWP':None, 'OOWP':None, 'RPI':None})
  # WP
  for team in teams:
    game_num = len(team['win_list']) + len(team['lose_list'])
    team['WP'] = len(team['win_list'])/float(game_num)

  # OWP
  for n, team in enumerate(teams):
    ops = team['win_list'] + team['lose_list']
    total = 0
    for op in ops:
      win_cnt = teams[op]['win_count']
      lose_cnt = teams[op]['lose_count']
      if n in teams[op]['win_list']:
        win_cnt -= 1
      elif n in teams[op]['lose_list']:
        lose_cnt -= 1
      total += float(win_cnt) / float(win_cnt + lose_cnt)
    team['OWP'] = total/float(len(ops))

  # OOWP
  for team in teams:
    ops = team['win_list'] + team['lose_list']
    total = sum([teams[elem]['OWP'] for elem in ops])
    team['OOWP'] = total/float(len(ops))

  for team in teams:
    team['RPI'] = 0.25 * team['WP'] + 0.5 * team['OWP'] + 0.25 * team['OOWP']

  print "Case #%d:" % (c+1,)
  # print teams
  for team in teams:
    # print team
    print team['RPI']

