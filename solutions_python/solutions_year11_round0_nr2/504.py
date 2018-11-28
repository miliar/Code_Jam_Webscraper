inf = open('B-large.in', 'r')
outf = open('magicAns.txt', 'w')

T = int(inf.readline())
for i in xrange(T):
	print i
	change = {'Q':{},'W':{}, 'E':{}, 'R':{}, 'A':{}, 'S':{}, 'D':{}, 'F':{}}
	oppose = {'Q':{},'W':{}, 'E':{}, 'R':{}, 'A':{}, 'S':{}, 'D':{}, 'F':{}}
	c = inf.readline()
	c = c.split()
	k = 1
	for j in xrange(1,int(c[0])+1):
		change[c[j][0]][c[j][1]] = c[j][2]
		change[c[j][1]][c[j][0]] = c[j][2]
		k += 1
	for j in xrange(k+1, k + int(c[k])+1):
		oppose[c[j][0]][c[j][1]] = 1
		oppose[c[j][1]][c[j][0]] = 1
		k += 1
	
	word = c[k+2]
	ans = word[0]
	curoppose = {}
	for j in xrange(1, len(word)):
		try:	
			t = change[ans[-1]][word[j]]
			ans = ans[:-1] + t
			
		except:
			try:
				m = {}
				try:
					m.update(oppose[ans[-1]])
				except:
					None
				try:
					m.update(curoppose)
				except:
					None
				if m[word[j]]:
					ans = ''
					curoppose = {}
			except:				
				ans += word[j]
				try:	
					curoppose.update(oppose[ans[-2]])
				except:
					None
	ans = list(ans)		
	outf.write('Case #' + str(i+1) + ': [' + ', '.join(ans) + ']\n')

inf.close()
outf.close()
		
