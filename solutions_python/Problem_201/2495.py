def printfun(i, ma , mi):
	print "case #{}: {} {}".format(i,ma , mi)

def div(num):
	global ls, rs, count

	if num%2 == 0: 
		ls.append((num/2)-1)
		rs.append(num/2)
	else:
		ls.append((num/2))
		rs.append(num/2)
	count += 1
	
	
def maxi():
	global ls, rs
	m = max(max(ls),max(rs))
	if m == max(ls):
		return ls.pop(ls.index(max(ls)))
	else:
		return rs.pop(rs.index(max(rs)))
	
t = int(raw_input())
for i in xrange(1, t+1):
	inp , k = [int(s) for s in raw_input().split(" ")]
	temp = inp
	ls = [temp]
	rs = [0]
	count = 0
	if k != temp:
		for j in xrange(k):
			val = maxi()
			div(val)
		if k == count:
			printfun(i,rs[-1], ls[-1])
	else:
		printfun(i,0,0)
