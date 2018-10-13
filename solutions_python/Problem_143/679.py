rf = open("input.txt", "r")
wf = open("output.txt", "w+")
numCases = int(rf.readline())

for i in range(numCases):
  a, b, k = (int(s) for s in rf.readline().split())
  numwins = 0
  for j in range(a):
    for h in range(b):
      if k > (j&h):
        numwins += 1
  wf.write("Case #{}: {}\n".format(i+1, numwins))
