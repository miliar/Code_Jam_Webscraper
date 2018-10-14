import gcj, bisect

def add(lengths, counts, s):
	if s in counts:
		counts[s] = counts[s] + 1
	else:
		counts[s] = 1

	ix = bisect.bisect_left(lengths, s)	
	if ix == len(lengths) or lengths[ix] != s:
		bisect.insort(lengths, s)

ifile, ofile = gcj.get_files('C')

T = int(ifile.readline().strip())
count = {}
for t in range(T):
	(N, K) = list(map(int, ifile.readline().split()))

	lengths = [N]
	counts  = {N : 1} 
	for i in range(K):
		#print(i, lengths, counts)

		l1 = lengths[-1]

		if len(lengths) == 1:
			l = l1
		else:
			l2 = lengths[-2]
			mn1 = (l1 - 1) // 2
			mx1 = l1 // 2
			mn2 = (l2 - 1) // 2
			mx2 = l2 // 2

			if mn1 > mn2:
				l = l1
			elif mn1 < mn2:
				l = l2
			else:
				if mx1 > mx2:
					l, mn, mx = l1, mn1, mx1
				else:
					l, mn, mx = l2, mn2, mx2
		#print("Choosen length", l)
		mn = (l - 1) //2
		mx = l // 2

		#Remove big length
		cnt = counts[l]
		if cnt == 1:
			del counts[l]
			lengths.remove(l)
		else:
			counts[l] = counts[l] - 1

		#Add two smaller lengths
		s1 = (l - 1) // 2
		s2 = l - 1 - s1
		if s1 > 0:
			add(lengths, counts, s1)
		if s2 > 0:
			add(lengths, counts, s2)

	ans = str(mx) + " " + str(mn)
	gcj.print_answer(ofile, t, ans)