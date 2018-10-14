import sys
import itertools

sys.stdin = open("cj1b_1-in-small.txt")

lines = map(lambda l: l.strip(), list(sys.stdin))

def most_common(L):
  groups = itertools.groupby(sorted(L))
  def _auxfun((item, iterable)):
    return len(list(iterable)), -L.index(item)
  return max(groups, key=_auxfun)[0]

def scan(word):
  struct = []
  prev = None
  count = 0
  for letter in word:
    if letter != prev:
      if prev != None: struct.append((prev, count))
      prev = letter
      count = 1
    else:
      count += 1
  struct.append((prev, count))
  return struct

def eq(a, b):
  if len(a) != len(b): return False
  for i in range(0, len(a)):
    if a[i][0] != b[i][0]: return False
  return True

def check(i, words, min_used, max_used):
  min_tot = 0
  max_tot = 0
  for word in words:
    letter, count = word[i]
    min_tot += count - min_used
    max_tot += max_used - count
  
  return min(min_tot, max_tot)

def solve(words):
  words = map(scan, words)
  letters_n = len(words[0])
  words_n = len(words)
  best = [sys.maxint] * letters_n
  
  prev = None
  for word in words:
    if prev != None and not eq(word, prev):
      return "Fegla Won"
    prev = word
  
  for i in xrange(0, letters_n):
    best_worst = sys.maxint
    best_worst_i = None
    bests = []
    
    for j in xrange(0, words_n):
      worst = 0
      _, count = words[j][i]
      
      for k in xrange(0, words_n):
        worst = max(worst, abs(count - words[k][i][1]))
      
      if worst < best_worst:
        bests = [(worst, count)]
        best_worst = worst
      elif worst == best_worst:
        bests.append((worst, count))
    
    best[i] = most_common(bests)
  
  moves = 0
  for word in words:
    for i in xrange(0, letters_n):
      letter, count = word[i]
      moves += abs(count - best[i][1])
      
  return moves
  # total = 0
  # for i in xrange(0, len(min_used)):
  #   total += check(i, words, min_used[i], max_used[i])
  
  # return total
      

t = int(lines[0])
i = 1
for j in xrange(0, t):
  n = int(lines[i])
  words = lines[i+1:i+n+1]
  i += n+1
  print "Case #%d: %s" % ((j + 1), solve(words))
