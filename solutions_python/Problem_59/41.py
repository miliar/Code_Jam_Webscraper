infile = open('A-large.in','r')
outfile = open('A-large.out','w')

T = int(infile.readline().strip('\n'))

for i in range(1,T+1):
  d = ['geoffreypascoe']
  line = infile.readline().strip('\n')
  tokens = line.split()
  N = int(tokens[0])
  M = int(tokens[1])
  
  for j in range(0,N):
    line = infile.readline().strip('\n')
    dirs = line.split('/')[1:]
    currentDir = d
    for dir in dirs:
      found = False
      for sub in currentDir[1:]:
        if sub[0] == dir:
          currentDir = sub
          found = True
      if not found:
        currentDir.append([dir])
        currentDir = currentDir[len(currentDir)-1]
  
  mkdirs = 0      
  for j in range(0,M):
    line = infile.readline().strip('\n')
    dirs = line.split('/')[1:]
    currentDir = d
    for dir in dirs:
      found = False
      for sub in currentDir[1:]:
        if sub[0] == dir:
          currentDir = sub
          found = True
      if not found:
        mkdirs += 1
        currentDir.append([dir])
        currentDir = currentDir[len(currentDir)-1]
        
  outfile.write("Case #" + str(i) + ": " + str(mkdirs) + "\n")
  
infile.close()
outfile.close()
        
    

