def dis(d):
	beg = 0
	end = d-1
	mid = (beg+end)/2
	return [max(mid-beg,end-mid),min(mid-beg,end-mid)]

def sol(n,k):
	res = []
	res.append(0)
	res.append(n+1)
	mi = 0
	ma = n+1

def sol_small(n,k):
	# if (k-1)>=(n+1)/2:
	# 	return [0,0]
	#else:
	sub = []
	i=0
	sub.append(n)
	while i!=k-1:
		sl = sub.pop(0)
		beg = 0
		end = sl-1
		mid = (beg+end)/2
		sub.append(end-mid)
		sub.append(mid-beg)
		i+=1
		sub.sort(reverse=True)
	return dis(sub[0])


f = open("C-small-1-attempt3.in")
wf = open("C-out.txt",'w')
data = []
for line in f:
	data.append(line)
cases = int(data[0])
for c in range(cases):
	p = data[c+1].split()
	n = int(p[0])
	k = int(p[1])
	res = sol_small(n,k)
	#print res
	wf.write("Case #%s: "%(c+1))
	wf.write(str(res[0]))
	wf.write(' ')
	wf.write(str(res[1]))
	wf.write('\n')