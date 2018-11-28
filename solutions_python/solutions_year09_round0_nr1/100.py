L, D, N = list( map ( lambda x: int(x), input().strip().split() ) )

language = []

for x in range(D): language.append( input() )
	
for x in range(N):
	pattern = input()	
	groups = []
	start, end, found = 0, 0, 0
	l = len(pattern)	
	while end < l:
		if pattern[end] == '(':
			start = end
			found = 1
		elif pattern[end] == ')':
			groups.append( pattern[start+1:end] )
			found = 0
		elif found == 0:
			groups.append( pattern[end] )
		end += 1
	count = 0
	for i in range(D):
		ok = True
		for j in range(L):
			if not language[i][j] in groups[j]: 
				ok = False
				break
		if ok: count += 1
	print("Case #{0}: {1}".format(x+1, count))
	