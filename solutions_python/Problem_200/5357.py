# 4
# 132
# 1000
# 7
# 111111111111111110

t = int(raw_input())
for i in xrange(1,t+1):
  n = int(raw_input())
  l = map(int,list(str(n)))
  # print l
  if int(''.join(sorted(str(n))))==n:
    print "Case #%d: %d"%(i,n)
  else:
    for x,y in zip(range(0,len(l)-1),range(1,len(l))):
      if l[x]>=l[y]:
        # print l[x],l[y]
        l[x] = l[x]-1
        # print l[x]
        # l[x] = 9
        for j in range(x+1,len(l)):
          l[j] = 9
        break
  
    # print   
    p = int(''.join(map(str,l)))
    print "Case #%d: %d"%(i,p)
  # print p
  # else:
  #   print "Case #%d: %d"%(i,check(n))

