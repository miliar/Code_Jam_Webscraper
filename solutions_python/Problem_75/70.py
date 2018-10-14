fin = open('in.txt', 'r')
fout = open('out.txt', 'w')
count = int(fin.readline().strip())
for i in range(count):
	words = fin.readline().strip().split(' ')
	
	idx = 0
	length = int(words[idx])
	c = {}
	for j in range(length):
		c[words[j+1][0]+words[j+1][1]] = words[j+1][2]
		c[words[j+1][1]+words[j+1][0]] = words[j+1][2]
	
	idx = length +1
	length = int(words[idx])
	r = {}
	for j in range (idx+1, idx+1+length):
		r[words[j][0]+words[j][1]] = ''
		r[words[j][1]+words[j][0]] = ''
	s = words[idx+1+length+1]
	#print c, r, s
	ret = []
	
	for j in range(0,len(s)):
		flag = True
		#print s[j]
		if j>0 and len(ret)>0:
			val = c.get('%s%s'%(ret[-1],s[j]), 'null')
			if val != 'null':
				#print val
				ret.pop(-1)
				ret.append(val)
				flag = False
			if flag:
				for k in range(len(ret)-1,-1,-1):
					if r.get('%s%s'%(ret[k],s[j]), 'null') != 'null':
						ret = []
						flag = False
						break
		if j==0 or flag:
			ret.append(s[j])
	
	fout.write( 'Case #%d: [%s]\n' % (i+1, ', '.join(ret)))