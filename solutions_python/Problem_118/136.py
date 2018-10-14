hf = []

def dfs(st, dep, tot):
	if dep>25: return
	if tot>=5: return
	for x in range(3):
		if 2*tot+x**2<10 and 2*dep+1<50:
			hf.append(st+str(x)+st[::-1])
		if 2*tot<10 and 2*dep<=50:
			hf.append(st+st[::-1])
	for x in range(3):
		st1 = st+str(x)
		dfs(st1, dep+1, tot+x**2)

def sq(x):
	st = ""
	for i in range(len(x)):
		count = 0
		for j in range(i+1):
			count += int(x[j])*int(x[i-j])
		st += str(count)
	return st[:len(x)-1]+st[::-1]


dfs("1",1,1)
dfs("2",1,4)

hf.append("1")
hf.append("2")
hf.append("3")
hf = list(set(hf))
hf = sorted(hf, key=lambda x: (len(x), [c for c in x]))

def comp(st1, st2):
	if len(st1)<len(st2): return True
	elif len(st1)>len(st2): return False
	else:
		for i in range(len(st1)):
			if st1[i]<st2[i]: return True
			elif st1[i]>st2[i]: return False
	return True

def binsearch(st):
	lo = 0
	hi = len(ful)-1
	ans = 0
	while True:
		if lo>hi: break
		mid = (lo+hi)/2
		if comp(ful[mid], st):
			lo = mid+1
			ans = mid
		else:
			hi = mid-1
	return ans

f = open("C-large-2.in", "r")
g = open("answer.txt", "w")

ful = []
for x in hf:
	ful.append(sq(x))
#num = int(data.readline())
	#ful.append(data.readline().split()[0])

N = int(f.readline())
for mm in range(N):
	x,y = f.readline().split()
	p = binsearch(x)
	q = binsearch(y)
	if ful[p]==x: p -= 1
	g.write("Case #{}: {}\n".format(mm+1, q-p))

f.close()
g.close()
