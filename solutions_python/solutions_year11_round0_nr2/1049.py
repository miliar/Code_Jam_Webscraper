# TODO: Small input + big O analysis for Large

def finelist(combine, opposed, invokations):
	l = []
	for invokation in invokations:
		l.append(invokation)
		try: l[-2] = combine[l[-2] + l[-1]]; del l[-1]
		except (IndexError, KeyError):
			try:
				if opposed[invokation] in l: l = []
			except KeyError: pass
	return l

T = int(input().rstrip())
for x in range(1, T+1):
	words = input().rstrip().split(' ')
	combine, opposed = {}, {}
	
	C = int(words[0]); del words[0]
	for s in words[:C]:
		combine[s[:2]] = s[2]
		combine[s[1] + s[0]] = s[2]
	del words[:C]
	
	D = int(words[0]); del words[0]
	for s in words[:D]:
		opposed[s[0]] = s[1]
		opposed[s[1]] = s[0]
	del words[:D]
	
	# N = int(words[0]); del words[0]
	# invokations = list(words[0])

	y = finelist(combine, opposed, words[1])
	print('Case #{}: [{}]'.format(x, ', '.join(y)))
