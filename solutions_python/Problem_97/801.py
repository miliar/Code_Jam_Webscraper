import fileinput

input = fileinput.input()

N = int(input.readline())

for i in (n+1 for n in range(N)):
  count = 0
  pairs = set()
  A, B = map(int,input.readline().strip().split(" "))
  for n in range(A,B):
    ns = str(n)
    for j in range(len(ns)):
      ms = ns[j:] + ns[:j]
      m = int(ms)
      if n < m <= B and not ms.startswith('0') and not (n,m) in pairs:
        pairs.add((n,m))
        count += 1
  print ("Case #{0}: {1}".format(i, count))
