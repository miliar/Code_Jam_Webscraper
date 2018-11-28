
f = open('in0.txt', 'r')

num_cases = int(f.readline())
case_num = 0
for line in f.readlines():
	case_num += 1
	#print line
	ch = line.strip().split()

	comb = []
	num_comb = int(ch.pop(0))
	
	for i in range(num_comb):
		comb.append((ch[0][0], ch[0][1], ch[0][2]))
		ch.pop(0)

	#print comb

	d = []
	num_d = int(ch.pop(0))
	for i in range(num_d):
		d.append((ch[0][0], ch[0][1]))
		ch.pop(0)

	#print d
	

	out = []
	seen_c = [-1]*num_comb
	seen_d = [[0,0]]*num_d

	#print seen_c
	#print seen_d

	n = []
	num_n = int(ch.pop(0))
	for c in ch[0]:
		did_something = False

		# combine
		for i, cc in enumerate(comb):
			if cc[0] == c:
				if seen_c[i] == 1 or (not seen_c[i] == -1 and cc[0] == cc[1]):
					did_something = True
					out.pop()
					out.append(cc[2])
					seen_c[i] = -1

					# fix d
					for i, dd in enumerate(d):
						# we saw cc[1], remove it
						if dd[0] == cc[1]:
							if seen_d[i][0] > 0:
								seen_d[i][0] -= 1
						if dd[1] == cc[1]:
							if seen_d[i][1] > 0:
								seen_d[i][1] -= 1
				else:
					seen_c[i] = 0
			elif cc[1] == c:
				if seen_c[i] == 0:
					did_something = True
					out.pop()
					out.append(cc[2])
					seen_c[i] = -1

					# fix d
					for i, dd in enumerate(d):
						# we saw cc[1], remove it
						if dd[0] == cc[0]:
							if seen_d[i][0] > 0:
								seen_d[i][0] -= 1
						if dd[1] == cc[0]:
							if seen_d[i][1] > 0:
								seen_d[i][1] -= 1
				else:
					seen_c[i] = 1
			else:
				seen_c[i] = -1

		if not did_something:
			# opposed: if we've seen a d
			for i, dd in enumerate(d):
				if dd[0] == c:
					if seen_d[i][1] > 0:
						did_something = True
						out = []
						seen_d[i] = [0,0]
						seen_c = [-1]*num_comb
					else:
						seen_d[i][0] += 1
				if dd[1] == c:
					if seen_d[i][0] > 0:
						did_something = True
						out = []
						seen_d[i] = [0,0]
						seen_c = [-1]*num_comb
					else:
						seen_d[i][1] += 1

		if not did_something:
			out.append(c)	

	out_str = ''
	out_str = 'Case #%d: [' % (case_num)
	for i in range(len(out)):
		out_str += out[i]
		if not i == len(out)-1:
			out_str += ', '
	out_str += ']'
	print out_str
