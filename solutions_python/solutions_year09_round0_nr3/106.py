from string import rjust
m="welcome to code jam"
for c in xrange(input()):
  s=raw_input().strip()
  l=len(s)
  ml=len(m)
  count=[[0 for j in xrange(ml)] for i in xrange(l)]
  if s[0]==m[0]: count[0][0]=1
  for i in xrange(1,l):
    for j in xrange(ml):
        if s[i]==m[j]:
            if j==0: count[i][j]=count[i-1][j]+1
            else: count[i][j]=(count[i-1][j-1]+count[i-1][j])%10000
        else:
            count[i][j]=count[i-1][j]
  print "Case #"+str(c+1)+": "+rjust(str(count[-1][-1]),4,"0")
