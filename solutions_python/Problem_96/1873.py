#! /usr/bin/python
# -*- coding: iso-8859-1 -*-

from itertools import product, combinations
from collections import defaultdict
import sys

def combinations_with_replacement(iterable, r):
  pool = tuple(iterable)
  n = len(pool)
  for indices in product(range(n), repeat=r):
    if sorted(indices) == list(indices):
      yield tuple(pool[i] for i in indices)

def get_possible_scores(num, surprising):
  return [i for i in range(num-(1+surprising), num+(2+surprising)) if i >= 0 and i <= 10]
  
def init_score_dict():
  scores = defaultdict(dict)
  for i in range(0, 11):
    for judges in combinations_with_replacement(get_possible_scores(i, True),3):
      diff = max(judges)-min(judges)
      if diff >= 3:
	continue
      elif diff == 2:
	key="surprising"
      else:
	key="normal"
      scores[sum(judges)][key] = sorted(judges)
  return scores
  
def process_score(scores, amt, surprising, best, judges):
  max_count = 0
  for c in combinations(range(amt), surprising):
    count = 0
    for i in range(amt):
      try:
	if max(scores[judges[i]]["surprising" if i in c else "normal"]) >= best:
	  count += 1
      except:
	continue
    max_count = max(max_count, count)
  return max_count
  
def process_line(line):
  s = [int(i) for i in line.split(" ")]
  return s[0], s[1], s[2], s[3:]


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "Invalid syntax. Please provide filename."
    sys.exit(2)
    
  fin=open(sys.argv[1],"r")
  fout = open(sys.argv[1].rsplit(".")[0] + ".out", "w")
  
  scores = init_score_dict()
  
  amt = int(fin.readline()[:-1])
  for i in range(amt):
    if i > 0:
      fout.write("\n")
    fout.write("Case #%d: %d"%(i+1, process_score(scores, *process_line(fin.readline().rstrip()))))
  fout.close()
  fin.close()
