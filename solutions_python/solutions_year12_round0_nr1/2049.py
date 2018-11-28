from sys import *

map = {
  'a': 'y',
  'b': 'h',
  'c': 'e',
  'd': 's',
  'e': 'o',
  'f': 'c',
  'g': 'v',
  'h': 'x',
  'i': 'd',
  'j': 'u',
  'k': 'i',
  'l': 'g',
  'm': 'l',
  'n': 'b',
  'o': 'k',
  'p': 'r',
  'q': 'z',
  'r': 't',
  's': 'n',
  't': 'w',
  'u': 'j',
  'v': 'p',
  'w': 'f',
  'x': 'm',
  'y': 'a',
  'z': 'q'
}

def solution(case, G):
  # solve S
  S = ""
  for g in G:
    if (map.has_key(g)):
      S += map[g]
    else:
      S += g
    
  print "Case #%d: %s" % (case+1, S)
  
T = int(raw_input())
for case in xrange(T):
  G = stdin.readline().strip()
  solution(case, G)