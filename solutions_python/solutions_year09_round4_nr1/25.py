import sys
fi=open(sys.argv[1],"r")
fo=open(sys.argv[2],"w")
tests=int(fi.readline())
for test in range(tests):
  n=int(fi.readline())
  matrix=[]
  for i in range(n):
    row=fi.readline()
    for j in range(n):
      if row[n-1-j]=="1": break
    matrix.append(j)
  change=True
  changes=0
  while change:
    change=False
    for i in range(n):
      if matrix[i]<n-i-1:
        change=True
        j=i+1
        while matrix[j]<n-i-1: j+=1
        while j!=i:
          matrix[j-1],matrix[j]=matrix[j],matrix[j-1]
          changes+=1
          j-=1
  print "Case #%d: %d"%(test+1,changes)

fi.close()
fo.close()
