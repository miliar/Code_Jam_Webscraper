def traintimes(dep,arr):
	tn = 0
	for i in dep:
		#if len(arr) >0: print i, arr[0]
		if len(arr) == 0 or i < arr[0]:
			tn+=1
		else:
			arr.pop(0)
	return tn
		
def mins(s):
	a,b = ((int(i) for i in s.split(":")))
	return a*60+b


cases = int(raw_input())

for case in xrange(1,cases+1):
	turn = int(raw_input())
	na,nb = tuple(int(i) for i in raw_input().split())
	da,ab = [],[]
	for i in xrange(na):
		times = raw_input().split()
		p,q = [mins(i) for i in times]
		da.append(p)
		ab.append(q + turn)
	db,aa = [],[]
	for i in xrange(nb):
		times = raw_input().split()
		p,q = [mins(i) for i in times]
		db.append(p)
		aa.append(q + turn)
	da.sort()
	ab.sort()
	db.sort()
	aa.sort()
	#print da,ab
	#print db, aa
	ta,tb = traintimes(da,aa),traintimes(db,ab)
	print "Case #%d: %d %d" % (case, ta, tb)
		