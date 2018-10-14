from collections import deque

infile = open('C-small.in','r')
outfile = open('C-small.out','w')

T = int(infile.readline().strip('\n'))

for case in range(1,T+1):
  line = infile.readline().strip('\n')
  tokens = line.split()
  R = int(tokens[0])
  k = int(tokens[1])
  N = int(tokens[2])
  
  tokens = infile.readline().strip('\n').split()
  for i in range(0,N):
    tokens[i] = int(tokens[i])
  groups = deque(tokens)
  
  total = 0
  for i in range(0,R):
    passengers = 0
    for i in range(0,N):
      if groups[0] <= (k-passengers):
        passengers += groups[0]
        groups.append(groups.popleft())
      else:
        break
    total += passengers
  
  outfile.write('Case #' + str(case) + ": " + str(total) + "\n")
  
infile.close()
outfile.close()