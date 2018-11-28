from sys import stdin
import itertools
import math

for case in range(int(stdin.readline())):
	count = 0
	n = int(stdin.readline())
	carset = ''.join(c for c, _ in itertools.groupby(stdin.readline().strip())).split(' ')
	#carset = list(set(carset))
	#carset.sort()
	#print(carset)
	#carset.sort(reverse=True)
	#print(carset)
	s = {}
	possible = True
	for e in carset:
		if len(e) > 1 and e in s:
			possible = False
			break
		else:
			if e in s:				
				s[e] = s[e] + 1
			else:
				s[e] = 1
	factor = 1
	for e in s:
		factor *= math.factorial(s[e])

	if not possible:
		print('Case #{}: {}'.format(case + 1, 0))
	else:
		#print(s)
		perms = list(itertools.permutations(s))
		for perm in perms:
			used = set()
			#print(perm)
			string = ''.join(c for c, _ in itertools.groupby(''.join(perm)))
			#print(string)
			possible = True
			lastChar = ''
			for c in string:
				if lastChar == '':
					used.add(c)
					lastChar = c
				elif c != lastChar:
					used.add(lastChar)
					lastChar = c
					if c in used:
						possible = False
						break
			if possible:
				count += 1 
		ans = count * factor
		print('Case #{}: {}'.format(case + 1, ans))
	
