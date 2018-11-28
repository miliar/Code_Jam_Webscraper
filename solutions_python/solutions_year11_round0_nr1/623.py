from sys import stdin

t = int(stdin.readline())
ti = 1
for line in stdin:
	arr = line.split()
	n = int(arr[0])
	ans = 0
	last = 'Y'
	last_dist = 0
	pos = {'O' : 1, 'B': 1}
	for i in xrange(n):
		who = arr[2*i + 1]
		button = int(arr[2*i + 2])
		if last == who:
			x = abs(button - pos[who]) + 1
			last_dist += x
			ans += x
		else:
			x = max(1, abs(button - pos[who]) + 1 - last_dist)
			last_dist = x
			ans += x			
		pos[who] = button
		last = who
		
	print 'Case #' + str(ti) + ': ' + str(ans)
	ti += 1
		
		
		
	
