#!/usr/bin/python

import sys

def parse(f):
  L, D, N = map(int, f.readline().rstrip().split(' '))
  words = []
  for d in range(D):
    words.append(f.readline().rstrip())
  pats = []
  for n in range(N):
    pats.append(pat2sets(f.readline().rstrip()))
  
  return (L, D, N, words, pats)

def match(word, pat):
  return reduce(lambda b, ch2set: b and ch2set[0] in ch2set[1], zip(word, pat), True)

def pat2sets(s):
  p = []
  state = 1 # 1-accept char, 2-in chars set
  for ch in s:
    if ch == '(':
      state = 2
      p.append(set())
    elif ch == ')':
      state = 1
    else:
      if state == 1:
        p.append(set(ch))
      else:
        p[-1].add(ch)
  return p

def main():
  f = sys.stdin
  L, D, N, words, pats = parse(f)
  # print L, D, N, words, pats
  for i in range(N):
    pat = pats[i]
    print 'Case #%d: %s' % (i+1, sum(map(lambda word: match(word, pat), words)))

if __name__ == '__main__':
  main()
