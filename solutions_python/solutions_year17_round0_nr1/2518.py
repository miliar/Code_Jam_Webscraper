# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  n = list(n)
  m = int(m)
  flips = 0
  for j in xrange(len(n)):
    if (j+m>len(n)):
        if ( '-' in n ):
            flips = 'IMPOSSIBLE'
        break
    if (n[j] == '+'): continue
    flips = flips + 1
    for k in xrange(j, j+m):
        n[k] = '+' if n[k] == '-' else '-'
        
    j = j + 1
  
  print "Case #{}: {}".format(i, flips)
  # check out .format's specification for more formatting options
  
