
infile = open("input.in")
outfile = open("output.out", 'w')

caseCount = int(infile.readline())

caseNum = 1
while (caseNum <= caseCount):
   answer = 0 
   nm = infile.readline().split(" ")
   nmax = int(nm[0])
   mmax = int(nm[1])

   levelParts = {}
   levelParts[0] = set([''])
   n = 0
   m = 0
   while (n < nmax):
      existsPath = infile.readline()
      parts = existsPath.strip().split('/') 
      level = 0
      for p in parts:
         ps = "/".join(parts[:level+1])
         if (level in levelParts):
            levelParts[level].add(ps)
         else:
            levelParts[level] = set([ps])
         level = level + 1
      n = n + 1

   print levelParts
   while (m < mmax):
      wantedPath = infile.readline()
      parts = wantedPath.strip().split('/') 
      level = 0
      for p in parts:
         ps = "/".join(parts[:level+1])
         if (level in levelParts):
            if ps not in levelParts[level]:
               answer = answer + 1
               levelParts[level].add(ps)
         else:
            levelParts[level] = set([ps])
            answer = answer + 1
         level = level + 1
      m = m + 1
   outfile.write("Case #" + str(caseNum) + ": " + str(answer) +"\n")
   caseNum = caseNum + 1

infile.close()
outfile.close()
