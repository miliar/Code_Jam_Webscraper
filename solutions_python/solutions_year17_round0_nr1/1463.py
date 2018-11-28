def solve(n,m):
	k= int(m)
	ans =0
	for i in range(0,len(n)-k+1):
		if n[i]=="-":
			for j in range(i,i+k):
				if n[j]=="-":
					n = n[0:j] + "+" + n[j+1:]
				else :
					n = n[0:j] + "-" + n[j+1:]
			ans =ans +1
	for i in range(len(n)):
		if n[i] == "-":
			return "IMPOSSIBLE"
	return ans

t = int(raw_input()) 
for i in xrange(1, t + 1):
  n, m = [s for s in raw_input().split(" ")]
  print "Case #{}: {}".format(i,solve(n,m))
  