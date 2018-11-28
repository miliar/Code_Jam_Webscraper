tests = int(raw_input())
for j in range(tests):
	maks, streng = raw_input().split(" ")
	maks = int(maks)
	level = [int(k) for k in streng]
	counter = 0
	standing = 0
	for i in range(maks+1):
		if level[i] !=0 and standing < i:
			counter += i - standing
			standing += i-standing
		standing += level[i]
	print 'Case #{}: {}'.format(j+1,counter)