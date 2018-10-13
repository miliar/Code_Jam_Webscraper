import sys
from multiprocessing import Pool

def solve(arg):
	a = arg[0]
	n = arg[1]
	sizes = arg[2]
	sizes.sort()
	
	cost = 0
	l = 0
	curSize = a
	while (l < len(sizes)):
		if curSize > sizes[l]:
			curSize += sizes[l]
			l += 1
		else:
			#cannot eat any more - either remove all to the end, or insert enough to be able to eat the next one
			removeCost = len(sizes) - l
			if curSize > 1:
				inserted = simulateInsert(curSize, sizes[l])
				insertCost = len(inserted)
			else:
				insertCost = sys.maxint
			print("Remove = %d, insert=%d" % (removeCost, insertCost))
			if (insertCost < removeCost):
				ipc = 0
				for ip in inserted:
					sizes.insert(l + ipc, ip)
					curSize += ip
					ipc += 1
				l += ipc
				cost += insertCost
			else:
				cost += removeCost
				break;
	return cost
	
def simulateInsert(curSize, nextSize):
	print("Simulate %d %d" % (curSize, nextSize))
	cs = curSize
	inserted = []
	while cs <= nextSize:
		inserted.append(cs - 1)
		cs += cs - 1
	print(inserted)
	return inserted

def solvePar(args):
	p = Pool(4)
	res = p.map(solve, args)
	return res
	
	
f = open(sys.argv[1])
o = open("p1.out","w")
with f:
	with o:
		args = []
		t = int(f.readline())
		for i in range(0,t):
			line = f.readline()
			a,n = map(lambda p:int(p), line.split(" "))
			line = f.readline()
			sizes = map(lambda p:int(p), line.split(" "))
			args.append((a,n,sizes))

		res = []
		for arg in args:
			res.append(solve(arg))
		i = 0
		for r in res:
			o.write("Case #%d: %s\n" % (i+1, r))
			i += 1
