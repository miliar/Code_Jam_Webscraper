
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b
  
def solve(line):
  n = int(line[0])
  tis = [int(ti) for ti in line[1:]]
  t = reduce(gcd,[(a-b) for a in tis for b in tis if a>b])
  fact = divmod(tis[0],t)
  if fact[1] == 0:
    return fact[0]*t - tis[0]
  else:
    return (fact[0]+1)*t - tis[0]

if __name__ == "__main__":
  i = 0
  for line in open("B-large.in"):
    if i > 0:
      line1 = line.split()
      print "Case #%s: %s" % (i, solve(line1))
    i += 1