#!/usr/bin/env python

T = int(raw_input())

for case in xrange(T):

  n = int(raw_input())
  
  naomi = map(float, raw_input().split())
  ken = map(float, raw_input().split())

  naomi.sort()
  ken.sort()

  nao_nao = list(naomi)
  ken_ken = list(ken)

  points_naomi = 0
  points_ken = 0

  for ii in xrange(n):
    temp_ken = ken.pop()

    if temp_ken > naomi[-1]:
      naomi.pop(0)
    else:
      naomi.pop()
      points_naomi += 1
      
  for ii in xrange(n):
    temp_nao = nao_nao.pop()

    if temp_nao > ken_ken[-1]:
      ken_ken.pop(0)
    else:
      ken_ken.pop()
      points_ken += 1
      
  print 'Case #' + str(case+1) + ':', points_naomi, n-points_ken
