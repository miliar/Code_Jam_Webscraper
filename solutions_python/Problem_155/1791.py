IN = open("in", 'r')
OUT = open("out", 'w')

n = IN.readline()

for x in xrange(0, int(n)):
  line = map(str, IN.readline().strip().split(' ')) 
  ans = 0
  maxS = int(line[0])
  line = line [1]
  count = 0  
  for p in xrange(0, maxS+1):
    if (count < p):
      invited = p - count
      ans += invited
      count += invited
    count += int(line[p])
    if (count > maxS):
      break

  outline = "Case #" + str(x+1) + ": " + str(ans) + "\n"
  OUT.write(outline)


OUT.close()
IN.close()
