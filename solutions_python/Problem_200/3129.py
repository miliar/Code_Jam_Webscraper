cases=int(raw_input())
for c in xrange(1,cases+1):
	st=raw_input()
	ar=""
	for x in xrange(0,len(st)):
		if not st[x] in ar:
			ar+=st[x]
	if ar=='10':
		st= "".join(['9']*(len(st)-1))
	else:
		for n in xrange(1,len(st)):
			if int(st[n-1])<=int(st[n]):
				continue
			else:
				st=st[:n-1]+str(int(st[n-1])-1)+"".join(['9']*(len(st)-(n)))
				for l in range(n-1,0,-1):
					if int(st[l-1])>int(st[l]):
						st=st[:l-1]+str((int(st[l-1])-1))+"9"+st[l+1:]
				for z in xrange(0,len(st)):
					if st[z]!='0':
						break
					st=st[z+1:]
				break
	print "Case #"+str(c)+":",
	print st
	