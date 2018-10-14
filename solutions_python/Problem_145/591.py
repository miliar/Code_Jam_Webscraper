import math

def gcd(a, b):
  a, b = [max(a,b), min(a,b)]
  return b if not a % b else gcd(a-b, b)

fin = open("input", "r")
fout = open("output", "w")

t = int(fin.readline())

for test in range(t):
  p,q = [int(x) for x in fin.readline().split("/")]

  c = gcd(p,q)
  p,q = [p/c, q/c]
  print(p,q,c)
  if int(math.log(q)/math.log(2)) == math.log(q)/math.log(2):
    k = 0
    while p/q < 1:
      p *= 2
      k += 1
    fout.write("Case #%d: %i\n" % (test+1, k))
  else:
    fout.write("Case #%d: impossible\n" % (test+1))

fin.close()
fout.close()
