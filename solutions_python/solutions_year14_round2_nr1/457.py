median=lambda d:(lambda t,n:t[n]+t[-n-1])(sorted(d),len(d)//2)/2

def str2tab(line):
	tab = {}
	order=0
	for x in range(len(line)):
		key = line[x]+str(order)
		if key in tab :
			tab[key]=tab[key]+1
		else:
			order = order + 1
			key = line[x]+str(order)
			tab[key]=1

	return tab

def check(ar):
	lst = ar[0].keys()
	for x in xrange(1,len(ar)):
		if lst != ar[x].keys():
			return False
	return True

def count(ar):
	per = {}
	for elem in ar:
		for key, el in elem.iteritems():
			try:
				per[key].append(el)
			except Exception, e:
				per[key] = []
				per[key].append(el)
	mov = 0
	for key,tab in per.iteritems():
		med = median(tab)
		for x in tab:
			mov = mov +abs(med-x)
	return mov
		

f = open('input.in')
out = open('output','w')
lines = f.readlines()
T = int(lines[0]) #read T
nbr = 0
for i in range(T):
	nbr = nbr + 1
	N = int(lines[nbr])
	nbr = nbr + 1
	ar = []
	for j in xrange(nbr,nbr+N):
		ar.append( str2tab(lines[j].rstrip('\n')))
	if(check(ar)):
		out.write("Case #%d: %d\n"%(i+1,count(ar)))
	else:
		out.write("Case #%d: Fegla Won\n"%(i+1))
	nbr = nbr+N-1

	
	# print "Case #%d: %d %d"%(i+1, dwar, N-war+diff)
f.close()
out.close()

