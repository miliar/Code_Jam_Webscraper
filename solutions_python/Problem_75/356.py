import sys

t = int(sys.stdin.readline())

answer = 1

for line in sys.stdin:
  words = line.split()
  c = int(words[0])
  combos = words[1:1+c]
  d = int(words[1+c])
  oppositions = words[2+c:2+c+d]
  n = int(words[2+c+d])
  seq = words[3+c+d]

  cur = []
  for x in seq:
    cur.append(x)
    #print cur
    if len(cur) >= 2:
      for combo in combos:
        if len(cur) >= 2:
          if (cur[-1] == combo[0] and cur[-2] == combo[1]) or (cur[-1] == combo[1] and cur[-2] == combo[0]):
            cur.pop()
            cur.pop()
            cur.append(combo[2])
      if len(cur) >= 2:
        for opp in oppositions:
          if (cur[-1] == opp[0] and opp[1] in cur) or (cur[-1] == opp[1] and opp[0] in cur):
            cur = []
            break
  print "Case #{}: [{}]".format(answer, ", ".join(cur))
  answer += 1

