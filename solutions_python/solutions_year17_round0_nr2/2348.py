fo = open('result_big.txt','w')
with open('B-large.in.txt') as f:
	lines = f.readlines()
	for i,line in enumerate(lines[1:]):
		s = line.strip()
		if len(s)==1:
			res = s
		else:
			need_edit = False
			for c in range(len(s)-1):
				if s[c]>s[c+1]:
					need_edit = True
					break
			if not need_edit:
				res = s
			else:
				#go backward
				while c-1>=0 and s[c]==s[c-1]:
					c = c-1
				if c==0 and s[c]=='1':
					res = '9'*(len(s)-1)
				else:
					pre = str(int(s[:c+1])-1)
					res =  pre + '9'*(len(s) - len(pre))

		fo.write('Case #{}: {}\n'.format(i+1, res))

fo.close()