fs={1:True,4:True, 9:True, 121:True, 484:True}

for i in xrange(int(raw_input())):
     a,b=raw_input().split()
     c=0
     for t in fs:
	  if t>=int(a) and t<=int(b):
	       c+=1
     print "Case #"+str(i+1)+":",c