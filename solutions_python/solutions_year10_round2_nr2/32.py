infile = open('B-large.in','r')
outfile = open('B-large.out','w')

C = int(infile.readline().strip('\n'))

for case in range(1,C+1):
  line = infile.readline().strip('\n')
  tokens = line.split()
  N = int(tokens[0])
  K = int(tokens[1])
  B = int(tokens[2])
  T = int(tokens[3])
  
  X = infile.readline().strip('\n').split()
  V = infile.readline().strip('\n').split()
  
  if K > N:
    outfile.write("Case #" + str(case) + ": IMPOSSIBLE\n")
  else:
    count = 0
    swaps = 0
    for i in range(N-1,-1,-1):
      P = int(X[i]) + int(V[i]) * T
      if P >= B:
        swaps += (N-i-1-count)
        count += 1
      if count >= K:
        break
    
    if count >= K:
      outfile.write("Case #" + str(case) + ": " + str(swaps) + "\n")
    else:
      outfile.write("Case #" + str(case) + ": IMPOSSIBLE\n")

outfile.close()
infile.close()