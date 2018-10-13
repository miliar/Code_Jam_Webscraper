class Dirr:
    def __init__(self, nm):
	self.name = nm
	self.list = []

T = int(raw_input())
for t in range(1, T+1):
    N, M = map(int, raw_input().split())
    d = Dirr('')
    for i in range(N):
	s = raw_input()
	a = s.split('/')[1:]
	j = 0
	dr = d
	while j < len(a):
	    for k, v in enumerate(dr.list):
		if v.name==a[j]:
		    dr = dr.list[k]
		    j = j + 1
		    break
	    else:
		while j < len(a):
		    #print "add"
		    dr.list.append(Dirr(a[j]))
		    dr = dr.list[-1]
		    j = j + 1
    sum = 0
    for i in range(M):
	s = raw_input()	
	a = s.split('/')[1:]
	#print a
	dr = d
	j = 0
	while j < len(a):
	    for k, v in enumerate(dr.list):
		#print v.name, a[j]
		if v.name==a[j]:
		    dr = dr.list[k]
		    j = j + 1
		    break
	    else:	
		sum = sum + (len(a) - j)
		while j < len(a):
		    dr.list.append(Dirr(a[j]))
		    dr = dr.list[-1]
		    j = j + 1
    print "Case #%d: %d" % (t, sum)
