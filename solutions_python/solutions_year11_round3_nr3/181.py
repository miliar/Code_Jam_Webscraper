inf = open('C-small-attempt0.in', 'r')
outf = open('cAns.txt', 'w')




T = int(inf.readline())
for j in xrange(T):
	print j+1
	N, L, H = map(int, inf.readline().split())
	sounds = map(int, inf.readline().split())
	sounds.sort()
	sounds.append('')
	for i in xrange(L, H+1):
		good = i
		next = sounds[0]
		k = 0
		while (next < i):
			if i%next != 0:
				good = -100
				break
			k+=1
			next = sounds[k]
		if good<0:
			continue
		next = sounds[k]
		d = len(sounds)
		while (k < d-1):
			print next, 'next', i
			if next%i != 0:
				good = -100
				break
			k+=1
			next = sounds[k]
		if good > 0:
			break
	print good
	outf.write('Case #' + str(j+1) + ': ')
	if good<0:
		outf.write('NO\n')
	else:
		outf.write(str(good) + '\n')
	
	
inf.close()
outf.close()		