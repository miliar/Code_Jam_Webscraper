testcases = open('A-large.in').read().strip().split('\n')
fout = open("output.txt","w")

N = int(testcases[0])
for x in range(N):
  a, b = testcases[x+1].split(' ')

  tot, n = 0, 0
  for k in range(len(b)):
    y = int(b[k])
    if tot < k:
      n += k-tot
      tot = k

    tot += y

  print >>fout, "Case #" + str(x+1) + ":", n
