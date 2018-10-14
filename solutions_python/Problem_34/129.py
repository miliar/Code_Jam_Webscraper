
# python 3.0



L,D,N = [int(v) for v in input().split()]

d = []
for i in range(D):
	d += [input()]

for i in range(1,N+1):
	line = input()
	
	toks = []
	inbracks = False
	curr = ""
	for c in line:
		if not inbracks:
			if c=='(':
				inbracks = True
			else:
				toks += [c]
		else:
			if c==')':
				inbracks = False
				toks += [curr]
				curr = ""
			else:
				curr += c
	
	
	valid = [w for w in d]
	for j in range(L):
		valid = [w for w in valid if (w[j] in toks[j])]
	
	count = len(valid)
	
	
	
	print("Case #"+str(i)+": "+str(count) , end='')
	#print(toks)
	#print(valid)
	if i<N: print()













