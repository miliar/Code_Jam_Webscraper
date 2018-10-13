cases = int(raw_input())
w2cj = "welcome to code jam"
pos = {}
for i in xrange(len(w2cj)):
  if pos.has_key(w2cj[i]):
    pos[w2cj[i]].append(i)
  else:
    pos[w2cj[i]] = [i]

for i in xrange(1,cases+1):
  counts = [0]*len(w2cj)
  input = raw_input()
  for letter in input:
    if letter == 'w':
      counts[0] += 1
    elif letter in pos:
      for j in pos[letter]:
        counts[j] = (counts[j] + counts[j-1]) % 10000
  print "Case #%d: %04d" %(i, counts[-1])

