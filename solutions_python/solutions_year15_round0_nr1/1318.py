fr = open('in', 'r')
fw = open('out', 'w')
t = int(fr.readline().strip())

for case in range(t):
	line = fr.readline().strip()
	num, s = line.split(' ')
	num = int(num)
	ans = 0
	cnt = 0
	for i in range(num+1):
		if int(s[i]) > 0 and cnt < i:
			ans += i - cnt
			cnt += ans
		cnt += int(s[i])
	print 'Case #%d: %d' % (case+1, ans)
	fw.write('Case #%d: %d\n' % (case+1, ans))
fr.close()
fw.close()