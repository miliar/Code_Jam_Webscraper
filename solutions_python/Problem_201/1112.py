d = {}

#d[1] = 3
#del d[1]

def divid(n, k) :
	i = 0
	d[n] = 1
	idx = 0
	
	while(True):
		mk = max(d.keys(), key=int)
		
		if (idx + d[mk] >= k):
			return mk

		idx += d[mk]

		tmp = d[mk]
		del d[mk]
		
		mk_1 = (int)((mk-1)/2)
		mk_2 = (mk-1) - mk_1
		
		if mk_1 in d:
			d[mk_1] += tmp
		else:
			d[mk_1] = tmp
			
		if mk_2 in d:
			d[mk_2] += tmp
		else:
			d[mk_2] = tmp

def lrmax(d):
	r = int((d-1)/2)
	l = (d-1) - r
	
	return str(l) + " " + str(r)

ret = divid(6, 2)

#print(d, ret)
#print("Case #" + str(0) + ": " + lrmax(ret))

tmp = input()

T = int(tmp)
#print(T)

for i in range(T):
	d.clear()
	tmp2 = input().split()
#	print(tmp2)
	ret = divid(int(tmp2[0]), int(tmp2[1]))
	print("Case #" + str(i+1) + ": " + lrmax(ret))

