import math

tests = int(raw_input())
for case in range(tests):
	arr = map(int, raw_input().split())
	n = arr[0]
	k = arr[1]
	
	h = int(math.log(n+1)/math.log(2))
	limit = 2**h
	
	if k < limit:
		
		commands = ""
		while k > 1:
			if k % 2 == 0:
				commands = 'L' + commands
				k /= 2
			else:
				commands = 'R' + commands
				k = (k-1)/2
		
		length = len(commands)
		
		h = length
		for step in range(length):
			mod = 2**h
			rem = (n - mod + 1) % mod
			if rem <= mod/2:
				x = (n - 1 - rem) / 2 + rem
				y = n - 1 - x
			else:
				x = (n - 1 - rem) / 2 + mod/2
				y = n - 1 - x
			h = h - 1
			if commands[step] == 'L':
				n = x
			else:
				n = y
					
		if n % 2 == 0:
			l = n/2
			r = l - 1
		else:
			l = (n-1)/2
			r = (n-1)/2
		print "Case #" + str(case + 1) + ":",l, r
	else:
		l = 0
		r = 0
		print "Case #" + str(case + 1) + ":",l, r