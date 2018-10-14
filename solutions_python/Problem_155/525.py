import sys

iFile = open(sys.argv[1],"r")

size = int(iFile.readline().strip())

for case in range(size):

  line = iFile.readline().strip().split()
  
  S_max = int(line[0])
  audience = line[1]

  standing = 0
  friends = 0

  for i,s in enumerate(audience):
    needed = max(0,i-standing)
    friends += needed
    standing += int(s)
    standing += needed

  output = str(friends)
  
  print("Case #"+str(case+1)+": "+output)
