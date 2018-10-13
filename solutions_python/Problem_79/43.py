#!/usr/bin/python

ri = raw_input

T = int(ri())
for t in xrange(T):
  n,m = map(int,ri().split())
  words = []
  for i in xrange(n):
    word = ri().strip()
    words.append(word)
  out = ["Case #%d:" % (t+1)]

  for j in xrange(m):
    cost = {}
    for word in words: cost[word] = 0
    l = ri().strip()
    used = {}
    for letter in l:
      hath = {}
      for word in words:
        if letter in word:
          pattern = "".join((x if x in used else "_") for x in word)
          hath[pattern] = 1
      for word in words:
        if letter not in word:
          pattern = "".join((x if x in used else "_") for x in word)
          if pattern in hath:
            cost[word] += 1
      used[letter] = 1
    best = words[0]
    maxcost = cost[best]
    for word in words:
      if cost[word] > maxcost:
        best = word
        maxcost = cost[best]
    out.append(best)
  print " ".join(out)

  
