import math

f = open('C-small-2-attempt1.in', 'r')
# f = open('C.txt', 'r')
fout = open('C-out.txt', 'w')


ncases = f.readline()
cases = f.readlines()

for i in range(len(cases)):
  ind = i+1
  fout.write("Case #%d: " %(i+1))
  n, k = cases[i].strip().split()
  n = int(n)
  k = int(k)

  log2 = int(math.floor(math.log(k,2)))
  div = float(n-k)/(2**(log2+1))
  fract = div%1
  ceil = int(math.ceil(div))
  if fract == 0:
    r, l = ceil, ceil
  elif fract >= 0.5:
    r, l = ceil, ceil-1
  else:
    r, l = ceil-1, ceil-1
  fout.write("%d %d\n" %(r, l))

  # print ("k=%d: %d %d" % (ind, r, l))