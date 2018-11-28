import math
global z
def calctree(gates, vals, node):
	global z
	i = node
	if(i < len(gates)):
		r1 = calctree(gates, vals, node*2+1)
		r2 = calctree(gates, vals, node*2+2)
		if(gates[i] == 0):
			return r1 | r2
		else:
			return r1 & r2
	else:
		i = int(math.log(node) / math.log(2))
		z = (node +1)% (len(gates)+1)
		ans = vals[z]
		#print node+1, ans
		return ans
	
def checktree(gates, perms, vals, m, v, i):
	global z
	ii = i
	temp = -1
	j=0
	ccount = 0
	gatesb = []
	for zzz in gates:
		gatesb += [zzz]
	while j<len(gates):
		if(perms[j] == 1):
			if(ii % 2 == 1):
				ccount += 1
				if gates[j] == 1:
					gatesb[j] = 0
				else:
					gatesb[j] = 1
			ii /= 2
		j += 1
		z = 0
	if(calctree(gatesb, vals, 0) == v): return ccount
	return 100000000000L

def booltree(gates, perms, vals, m, v):
	minc = 100000000000L
	ccount = 0
	for i in perms:
		if(i == 1): ccount += 1
	totc = 2 ** ccount
	i = 0
	while i <= totc:
		res = checktree(gates, perms, vals, m, v, i)
		if res < minc: minc = res
		i += 1
	return minc
	
n = int(raw_input())
for i in range(n):
	curinp = raw_input()
	curinp = curinp.split()
	m = int(curinp[0])
	v = int(curinp[1])
	gates = []
	perms = []
	for j in range((m-1)/2):
		curinp = raw_input()
		curinp = curinp.split()
		gates += [int(curinp[0])]
		perms += [int(curinp[1])]
	vals = []
	for j in range((m+1)/2):
		curinp = raw_input()
		curinp = curinp.split()
		vals += [int(curinp[0])]
	global z
	z = 0
	res = booltree(gates, perms, vals, m, v)
	print "Case #%d:" % (i+1), 
	if(res == 100000000000L):
		print "IMPOSSIBLE"
	else:
		print res

