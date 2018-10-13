import sys

mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', '\n':'', 'q':'z'}

def solveProblem():
  line = sys.stdin.readline()
  out = ""
  for c in line:
    out = out + mapping[c]
  return out

pcount = int(sys.stdin.readline())

for i in range(1, 1+pcount):
  print "Case #"+str(i)+":", solveProblem()
