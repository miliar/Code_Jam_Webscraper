def vovel(x):
 v = "aeiou"
 if x in v:
  return 0
 return 1
 

for _ in xrange(input()):

 #print str(_) + "<<<<<<<<<<"
 s,n = raw_input().split()
 n=int(n)
 a = [ ]
 now=0
 lens = len(s)
 for j in xrange(lens):
  i=s[j]
  a.append(vovel(i))
 #print a
 
 nub=0
 for i in xrange(lens):
  j=i
  now=0
  while(j<lens):
   if a[j]:
    now+=1
   else:
    now=0
   if now>=n:
    #print s[i:j],now
    nub+=lens-j
    break
   j+=1
   
   
 print "Case #"+str(_+1)+": "+str(nub)