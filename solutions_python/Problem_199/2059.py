t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  S,K = [s for s in raw_input().split(" ")]
  backup = [S]
  original_S = S
  Slist=list(S)
  k=int(K)
  r = 0 
  #print S 
  while S.count("+") < len(S):
	start = S.index("-")
	#if start < K: start = 0
	end = start + int(K) 
	inc = 1 
	#print "S:{}".format(S)
	#print " start: {}, end: {}, len: {}".format(start, end, len(S))
	
	if end < len(S)+1:
		for x in xrange(start,start+k):
			#print "x:{}".format(x)
			if S[x] == "-" : 
				Slist[x]="+"; 
			else:
				Slist[x]="-"
	if end > len(S):
		for x in xrange(-1,-(k+1),-1):
			#print "x:{}".format(x)
			if S[x] == "-" : 
				Slist[x]="+" 
			else: 
				Slist[x]="-"
				
	S = "".join(Slist)
	
	#print "S:{}".format(S)
	#print "original_S:{}".format(original_S)
	#if original_S == S: r = "IMPOSSIBLE"; break;
	if S in backup: r = "IMPOSSIBLE"; break;
	if S not in backup: backup.append(S)
	r=r+1

  

  print "Case #{}: {}".format(i, r)	