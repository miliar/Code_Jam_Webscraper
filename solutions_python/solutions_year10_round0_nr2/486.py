# -*- coding: utf-8 -*-
from collections import defaultdict
fname = "B-small-attempt2"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  linebits = [int(numb) for numb in linestr.split()]
  if len(linebits) == 1:
    return linebits[0]
  else:
    return linebits
    
def hcf(numbers):
  if len(numbers) == 1:
    return numbers[0]
  factor_sets = defaultdict(list)
  for number in numbers:
    i = 2
    while i <= int(number**0.5):
      index = 0
      while number % i == 0:
	index += 1
	number /= i
      if index:
	factor_sets[i].append(index)
      i += 1
    if number > 1:
      factor_sets[number].append(1)
  
  hcf = 1
  for factor in factor_sets:
    if len(factor_sets[factor]) < len(numbers):
      continue
    hcf *= factor**min(factor_sets[factor])
  return hcf
  
numcases = gcj_read()

for caseno in range(numcases):
  times = gcj_read()[1:]
  times.sort()
  timegaps = []
  previous = times[0]
  for time in times[1:]:
    if time != previous:
      timegaps.append(time-previous)
      previous = time
  T = hcf(timegaps)
  timeleft = T - (times[0] % T)
  if timeleft == T:
    timeleft = 0
  fout.write("Case #"+str(caseno+1)+": "+ str(timeleft) +"\n")

fin.close()
fout.close()