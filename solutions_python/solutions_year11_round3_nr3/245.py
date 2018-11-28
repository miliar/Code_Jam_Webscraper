fileName = "C-small-attempt5"
fin = open(fileName + ".in", "r")
fout = open(fileName + ".out", "w")

T = int(fin.readline())

def factors(n):
	return map(lambda x: x[0], list(factor(n)))

for caseID in xrange(1, T+1):
	N, L, H = map(int, fin.readline().split())
	k = list(set(map(int, fin.readline().split())))
	kgcd = reduce(gcd,k)
	dg = divisors(kgcd)
	check = False
	for i in dg:
		if (i >= L) and (i <= H):
			print "Case #%d: %d" % (caseID,i)
			fout.write("Case #%d: %d\n" % (caseID,i))
			check = True
			break
	if check:
		continue
	klcm = reduce(lcm,k)
	d = divisors(klcm/kgcd)
	for i in d:
		check = True
		ans = i * kgcd
		if (ans >= L) and (ans <= H):
			for j in k:
				if (mod(ans, j) != 0) and (mod(j, ans) != 0):
					check = False
					break
			if check:
				print "Case #%d: %d" % (caseID, ans)
				fout.write("Case #%d: %d\n" % (caseID, ans))
				break
	else:
		final = True
		finalAns = 1
		for i in xrange(L, H+1):
			check = True
			for j in k:
				if (mod(i, j) != 0) and (mod(j, i) != 0):
					check = False
					break
			if check:
				finalAns = i
				print i, kgcd
				print N, L, H
				print k
				final = False
				break
		if final:
			print "Case #%d: NO" % caseID
			fout.write("Case #%d: NO\n" % caseID)
		else:
			print "Case #%d: %d" % (caseID, finalAns)
			fout.write("Case #%d: %d\n" % (caseID, finalAns))

	'''
	print k
	fs = set() #factor set
	for i in k:
		for j in factors(i):
			fs.add(j)
	ansLo = prod(fs)
	ansHi = reduce(lcm, k)
	ans = -1
	for i in divisors(ansHi / ansLo):
		#print i
		if (ansLo*i >= L) and (ansLo*i <= H):
			check = True
			for j in k:
				if (mod((ansLo*i), j) != 0) and (mod(j, (ansLo*i)) != 0):
					check = False
					break
			if check:
				ans = ansLo * i
				break
	#print L, H, ans
	if (ans >= L) and (ans <= H):
		print "Case #%d: %d" % (caseID, ans)
		fout.write("Case #%d: %d\n" % (caseID, ans))
	else:5190
		print "Case #%d: NO" % caseID
		fout.write("Case #%d: NO\n" % caseID)
	if (ans > H):
		print "TOO HIGH"
		'''

fin.close()
fout.close()
