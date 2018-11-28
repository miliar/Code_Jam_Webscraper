fi = open('B-large.in','r')
fo = open('B-large.out','w')

T = int(fi.readline().strip())
for t_no in range(T):
	s = fi.readline().split(' ')
	C = int(s.pop(0))
	
	combine = {}
	for i in range(C):
		spell = s.pop(0)
		combine[spell[:2]] = spell[2]
		combine[spell[1]+spell[0]] = spell[2]
	
	D = int(s.pop(0))
	
	oppose = set()
	for i in range(D):
		spell = s.pop(0)
		oppose.add(spell)
		oppose.add(spell[1]+spell[0])
		
	N = int(s.pop(0))
	magic = s.pop(0).strip()
	result = ""
	stack = []
	if len(magic) < 2:
		result = str(list(magic)).replace("'","")
	elif C == 0 and D == 0:
		result = str(list(magic)).replace("'","")
	else:
		for i in range(N):
			add = 1
			call = magic[i]
			if stack == []:
				stack.append(call)
				continue
				
			spell = stack[-1] + call
				
			if spell in combine.keys():
				stack[-1] = combine[spell]
				add = 0
			elif D>0:
				for	j in range(len(stack)):
					spell = stack[j] + call
					if spell in oppose:
						stack = []
						add = 0
						break
			if add == 1:
				stack.append(call)
		result = str(stack).replace("'","")
		
	print result

	fo.write("Case #%d: %s\n" % (t_no + 1, result))
	
print "Done!"
fi.close()
fo.close()