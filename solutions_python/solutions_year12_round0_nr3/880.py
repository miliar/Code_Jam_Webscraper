
f = open(raw_input("Filename: "), 'r')
T = int(f.readline())

def getRotations(x):
  retList = []
  X = str(x)
  for i in range(len(X)):
    X = X[1:] + X[:1]
    if x < int(X):
      retList.append(int(X))
  return list(set(retList))

Results = []
for case in range(T): 
  line = map((lambda x: int(x)), f.readline().split(' '))
  A = line[0]
  B = line[1]
  count = 0
  for x in range(A, B+1):
    for y in getRotations(x):
      if y <= B:
          #print "(" + str(x) + "," + str(y) + ")"
          count += 1
  Results.append("Case #" + str(case+1) + ": " + str(count))

for x in Results:
  print x 
