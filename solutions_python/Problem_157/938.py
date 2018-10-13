fr = open('in','r')
fw = open('out','w')

com = {'0':0,'1':1, 'i':2, 'j':3, 'k':4}
mul = [ [0, 0, 0, 0, 0],
		[0, 1, 2, 3, 4],
		[0, 2,-1, 4,-3],
		[0, 3,-4,-1, 2],
		[0, 4, 3,-2,-1]
	  ]
div = [ [0, 1, 2, 3, 4],
		[0, 1,-2,-3,-4],
		[0, 2, 1,-4, 3],
		[0, 3, 4, 1,-2],
		[0, 4,-3, 2, 1]
	  ]

t = int(fr.readline().strip())
for case in range(t):
	ans = 'Yes'
	l, x = fr.readline().strip().split(' ')
	l = int(l)
	x = int(x)
	s = fr.readline().strip()
	s = s * x
	#print s
	s = [com[i] for i in s]
	#print s
	
	left = -1
	right = -1
	tmp = 1
	smb = 1
	for i in range(len(s)):
		if mul[tmp][s[i]] < 0:
			smb *= -1
		tmp = abs(mul[tmp][s[i]])
		if tmp*smb == 2:
			left = i
			break

	tmp = 0
	smb = 1
	#import pdb; pdb.set_trace()
	for i in range(1, len(s)):
		if div[tmp][s[len(s)-i]] < 0:
			smb *= -1
		tmp = abs(div[tmp][s[len(s)-i]])
		if tmp*smb == 4:
			right = len(s)-i
			break

	if left<0 or right<0:
		#print left, right
		ans = 'No'

	tmp = 1
	smb = 1
	for i in range(left+1, right):
		if mul[tmp][s[i]] < 0:
			smb *= -1
		tmp = abs(mul[tmp][s[i]])
	if tmp*smb != 3:
		ans = 'No'

	print 'Case #%d: %s' % (case+1, ans)
	fw.write('Case #%d: %s\n' % (case+1, ans))

fr.close()
fw.close()
