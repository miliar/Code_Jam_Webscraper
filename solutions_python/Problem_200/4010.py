n = int(raw_input())
for x in range(1,n+1):
	t = list(str(raw_input()))
	k = len(t)-1
	y = ""
	f = 0
	while k > 0:
		if int(t[k]) < int(t[k-1]):
			for i in range(k,len(t)):
				t[i]="9"
			t[k-1] = str(int(t[k-1])-1)

		k = k-1
		
	for i in t:
		y = y+i
	y = y.strip("0")
	print "Case #{}: {}".format(x,y)

