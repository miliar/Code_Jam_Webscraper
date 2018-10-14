

def funct(ar, mn, mx):
	if mx<10:
		return 0
	lres = 0
	wordlen = len(str(mx))

	while len(ar)>1:
		success = 0
		pretend = ar[0]
		pretend_str = str(pretend)
		#print pretend_str
		for j in xrange(1, wordlen):
			recycled_str = pretend_str[j:]+pretend_str[:j]
			#print recycled_str
			recycled = int(recycled_str)
			if recycled>=mn and recycled<=mx and recycled != pretend:
				lres +=1
				success += 1
				if success==2:
					lres +=1
				if success==3:
					lres +=2
				#print pretend, recycled
				if recycled in ar:
					ar.remove(recycled)
		ar.remove(pretend)

	return lres



T = input()

for i in xrange(0, T):
	data = raw_input()
	nabor = data.split(' ')	

	lmin = int(nabor[0])
	lmax = int(nabor[1])

	larray = range(lmin, lmax+1)

	#print(lmin, lmax, larray)

	lresult = funct(larray, lmin, lmax)		

	print 'Case #%(iteration)i: %(result)i'%{'iteration':i+1, 'result':lresult}