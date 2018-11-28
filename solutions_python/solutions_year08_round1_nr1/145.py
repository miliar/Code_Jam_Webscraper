ifp = open("input.txt", "r")
ofp = open("output.txt", "w")
num_test = int(ifp.readline())
for i in range(num_test):
  ifp.readline()
  v1 = map(int, ifp.readline().split())
  v2 = map(int, ifp.readline().split())
  v1.sort()
  v2.sort()
  v2.reverse()
  sum = 0
  for j in range(len(v1)):
    sum += v1[j] * v2[j]
  ofp.write("Case #%d: %d\n" % (i+1, sum))

ifp.close()
ofp.close()
