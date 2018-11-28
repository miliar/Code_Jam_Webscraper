t = int(raw_input()) 
for i in xrange(1, t + 1):
  d,n = [int(p) for p in raw_input().split(" ")]
  #print d,n
  k=[]
  s=[]
  for j in range(int(n)):
  	k1,s1=[int(p) for p in raw_input().split(" ")]
  	k.append(k1)
  	s.append(s1)
  #print k,s
  max=-1.0
  for j in range(int(n)):
  	if float(float(d-k[j])/s[j]) > max:
  		max = float(float(d-k[j])/s[j])
  #print max
  print "Case #{}: ".format(i)+"{0:.6f}".format(float(float(d)/max))
  