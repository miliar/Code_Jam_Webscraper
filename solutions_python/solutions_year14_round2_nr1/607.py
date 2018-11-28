infile = 'A-small-attempt1.in'
outfile = 'A-small-out.txt'

def fun(x, y):
  count = 0
  i = 0
  j = 0
  strx = ''
  stry = ''
  while i < len(x) and j < len(y):
    if x[i] == y[j]: 
      strx += x[i]
      stry += y[j]
      i += 1
      j += 1
    else: # something doesn't match, try to delete
      if i == 0 and j == 0:
        return -1
      while strx[-1] == x[i]:
        i += 1
        count += 1
      while stry[-1] == y[j]:
        j += 1
        count += 1
      if x[i] != y[j]:
        return -1
  while i < len(x):
    if x[i] == strx[-1]:
      count += 1
      i += 1
    else:
      return -1
  while j < len(y):
    if y[j] == stry[-1]:
      count += 1
      j += 1
    else:
      return -1
  return count


out = open(outfile, 'w')
with open(infile) as f:
  M = int(f.readline())
  for n in xrange(M):
    N = int(f.readline())
    strs = []
    for k in xrange(N):
      strs.append(f.readline())
    a = fun(strs[0], strs[1])
    if a == -1:
      out.write("Case #"+str(n+1)+": Fegla Won\n")
    else:
      out.write("Case #"+str(n+1)+": "+str(a)+"\n")

out.close()

