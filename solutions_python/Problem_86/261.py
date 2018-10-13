import sys
try:
	t = input()
	N = t+1
	while t>0:
		ans = []
		ans.append("Case")
		ans.append('#' + str(N-t) + ':')
		x = raw_input()
		a = []
		for i in x.split(' '):
			a.append(int(i))	
		n = a[0]
		l = a[1]
		h = a[2]
		M = []
		x = raw_input()
		for i in x.split(' '):
			M.append(int(i))
		x = l
		while x<=h:
			fl = 1
			for i in M:
				fl = 1
				if x%i == 0:
					fl = 0
				if i%x == 0:
					fl = 0
				if fl == 1:
					break	
			if fl == 0:
				ans.append(x)
				break;	
			x = x+1		
		if fl == 1:
			ans.append("NO")			
		print ans[0],ans[1],ans[2]
		t = t - 1
except:
	sys.exit(1)				