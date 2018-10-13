from collections import defaultdict

with open('in.txt','rb') as fin, open('output.txt','w') as fout:
	case = 1

	it = iter(fin.readlines())
	_ = next(it)

	for line in it:
		print ("\n\n\n")
		print ("case " + str(case))
		line = next(it)


		xs = [int(c) for c in line.split()]

		best = 10000000000
		for i in range(1,1001):
			spec = 0
			for x in xs:
				spec += (x+i-1)/i -1
			score = spec + i
			if score < best:
				best = score


		# #print (line)

		# h = defaultdict(int)
		# m=0
		# spec=0
		# for c in line.split():
		# 	h[int(c)] += 1
		# 	m = max(m,int(c))

		# best = m+spec


		# for i in range(m,2,-1):			
		# 	#print ([(n,q) for (n,q) in sorted(h.items(),reverse=True) if q>0])	
		# 	#print m+spec
		# 	if i in h:
		# 		if i%2==0:
		# 			h[i/2] += 2*h[i]
		# 		else:
		# 			h[(i-1)/2] += h[i]
		# 			h[(i-1)/2+1] += h[i]
		# 		spec += h[i]
		# 		h[i] = 0
		# 	while m>0 and h[m]==0:
		# 		m -= 1
			
		# 	#assert ([(n,q) for (n,q) in sorted(h.items(),reverse=True) if n>0][0] == m)
		# 	best = min(best,m+spec)

		fout.write("Case #" + str(case) + ": " + str(best) + "\n")
		case += 1