def ask3(n,m):
	sp = n
	sl = 1
	res = []
	while(m>0):
		if m<=sl:
			aux = sp%sl
			if aux>0 and aux>=m: sp = sp/sl
			else: sp = sp/sl-1
			if sp%2==1: res.append(sp/2+1)
			res.append(sp/2)
			return res
		else:
			m-=sl
			sp-=sl
			sl *=2
		

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #print(list(n)," ",m)
  res = ask3(n,m)
  print "Case #{}: {} {}".format(i,max(res),min(res))
  # check out .format's specification for more formatting options