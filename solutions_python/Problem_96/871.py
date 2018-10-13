# dancing.py
import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
  line_array = sys.stdin.readline().strip().split(' ')
  N = int(line_array[0]) # number of scores
  S = int(line_array[1]) # number of "surprising" scores
  p = int(line_array[2]) # how many people could have gotten this score or better?
  scores = [int(d) for d in line_array[3:]]
  # counting data
  count = 0
  maybes = 0
  for score in scores:
    triplet = [score/3,score/3,score/3]
    if score%3 >= 1: triplet[0]+=1
    if score%3 >= 2: triplet[1]+=1
    if triplet[0] >= p:
      count+=1
    elif triplet[0] == triplet[1] and triplet[0]+1 <= 10 and triplet[1]-1 >= 0 and triplet[0]+1 >= p:
      maybes+=1
  count += min(maybes,S)
  print "Case #%d: %d" % (t+1,count)
