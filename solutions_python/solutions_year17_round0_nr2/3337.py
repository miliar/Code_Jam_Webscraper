def subtract(N):
	L = len(N)
	if L==1:
		return N

	N = np.array([int(n) for n in list(N)])
	pivot = -1
 	prev = np.nan
	for i in range(L):
		curr = N[i]
		if curr<prev:
			pivot = i
		prev = curr
	if pivot==-1:
		return ''.join([str(n) for n in list(N)])

	#print pivot

	backtrack = 1
	for i in range(pivot):
		if pivot-i-1==0 or N[pivot-i-1]>N[pivot-i-2]:
			backtrack = pivot-i-1
			break

	#print backtrack

	N[backtrack]-=1
	N[backtrack+1:]=9
	return (''.join([str(n) for n in list(N)])).lstrip('0')

out_lines = []
with open('../B-small-attempt0.in') as f:
	for i,line in enumerate(f):
		if i>0:
			out = subtract(line.rstrip('\n'))
			out_lines.append('Case #'+str(i)+': '+out+'\n')

with open('B-small-attempt0.out','w') as f:
	for line in out_lines:
		f.write(line)

