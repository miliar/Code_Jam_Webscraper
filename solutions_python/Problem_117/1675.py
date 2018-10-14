def testArr(cl,cw,arr):
	for x in xrange(cl):
		for y in xrange(cw):
			v = arr[x][y]
			y1t = 1
			for y1 in xrange(cw):
				if arr[x][y1]>v:
					y1t = 0
			x1t = 1
			for x1 in xrange(cl):
				if arr[x1][y]>v:
					x1t = 0
			if((x1t==0) and (y1t==0)):
				return "NO"
	return "YES"
f = open("test.txt","r")
o = open("out.txt","w")
t = 0
i = 0
j = 0
cl = 0
cw = 0
arr = []
total = 0
h = 0
res = ""
for l in f:
	if i == 0:
		t = int(l.strip("\n"))
		j = 1
		i = 1
		h = 0
		continue
	if j == 1 or h==cl:
		# Getting things started
		t = l.strip("\n").split(" ")
		cl = int(t[0])
		cw = int(t[1])
		j = 0
		h = 0
		arr = [[0 for x in xrange(cw)] for x in xrange(cl)]
		marr = [[0 for x in xrange(cw)] for x in xrange(cl)]
		total = total + 1
		continue
	if h<cl:
		t = l.strip("\n").split(" ")
		hh = 0
		for e in t:
			arr[h][hh] = int(e)
			hh = hh + 1
		h = h + 1
		if h==cl:
			res = res + "Case #%d: %s\n" % (total,testArr(cl,cw,arr))
		continue
o.write(res.strip("\n"))
o.close()
f.close()