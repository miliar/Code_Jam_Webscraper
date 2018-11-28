t = int(raw_input())

name = ["GABRIEL", "RICHARD"]
p = 0
imp = 1
for i in xrange(t):
	print "Case #"+str(i+1)+":",
	a = map(int, raw_input().split())
	if a[0] == 1:
		print name[p]
	elif a[0] == 2:
		mx = max(a[1], a[2])
		if(a[1] % 2 == 0 or a[2] % 2 == 0):
			print name[p]
		else:
			print name[imp]
	elif a[0] == 3:
		mx = max(a[1], a[2])
		mn = a[1]+a[2]-mx
		if(mn >= 2 and (mx % 3 == 0 or mn % 3 == 0)):
			print name[p]
		else:
			print name[imp]

	else:
		if a[1]*a[2] >= 12:
			print name[p]
		else:
			print name[imp]
		
	
