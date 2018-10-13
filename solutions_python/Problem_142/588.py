t = int(raw_input())

for i in xrange(t):
	k = int(raw_input())
	count = 0
	all_str = []
	mini_str = []
	for j in xrange(k):
		st = list(raw_input())
		gen = []
		mini_st = ""
		ln = len(st)
		index = 0
		this_count = 0
		last_ch = ''
		
		while(index < ln):
			if index == 0:
				last_ch = st[index]
				mini_st += last_ch
				this_count = 1
			else :
				if st[index] == last_ch:
					this_count += 1
				else :
					gen.append([last_ch,this_count])
					last_ch = st[index]
					mini_st += last_ch
					this_count = 1
			index += 1

		gen.append([last_ch,this_count])
		all_str.append(gen)
		mini_str.append(mini_st)
	
	test = True

	ln = 0

	checker = mini_str[0]

	for j in xrange(1,k):
		if mini_str[j] != checker:
			test = False
			break
	
	print "Case #" + str(i+1) + ":",
	
	if not(test):
		print 'Fegla Won'
	else :
		ln = len(all_str[0])
		minimal = [100] * ln
		maximal = [0] * ln

		for j in xrange(k):
			for l in xrange(ln):
				if all_str[j][l][1] > maximal[l]:
					maximal[l] = all_str[j][l][1]
				if all_str[j][l][1] < minimal[l]:
					minimal[l] = all_str[j][l][1]
	
		for j in xrange(ln):
			count += maximal[j] - minimal[j]
		print count
	


