from __future__ import division
from fractions import Fraction

f = [l[:-1] for l in file("in")][1:]


lowest_whole = [0] * 101

for x in range(101):
  fr = Fraction(x, 100)
  lowest_whole[x] = fr.denominator


case = 0
for line in f:
  case += 1

  today, percent_today, percent_ever = [int(x) for x in line.split(" ")]

  possible = True

  if (percent_ever == 100 or percent_ever == 0) and percent_today != percent_ever:
    possible = False

  #check if today is right

  if today < lowest_whole[percent_today]:
    possible = False

  ans = "Possible" if possible else "Broken"
  print "Case #%d: %s" % (case, ans)

