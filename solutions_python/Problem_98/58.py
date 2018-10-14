import math

tests = input()
for ii in range(1,tests+1):
	[h,w,d] = map(int,raw_input().split())
	for y in range(h):
		line = raw_input()
		pos = line.find('X')
		if pos>-1:
			X=pos-0.5
			Y=y-0.5
	h-=2
	w-=2
	range_try = []
	for bigX in range(-d/(2*w)-1,d/(2*w)+2):
		for bigY in range(-d/(2*h)-1,d/(2*h)+2):
			x1 = bigX*2*w
			y1 = bigY*2*h
			x2 = x1-2*X
			y2 = y1-2*Y
			if x1**2 + y1**2 <= d**2:
				range_try.append((x1,y1))
			if x1**2 + y2**2 <= d**2:
				range_try.append((x1,y2))
			if x2**2 + y1**2 <= d**2:
				range_try.append((x2,y1))
			if x2**2 + y2**2 <= d**2:
				range_try.append((x2,y2))
	range_try.remove((0,0))
	sol = map(lambda(x,y):math.atan2(x,y),range_try)
	solution = len(set(sol))
	print "Case #"+str(ii)+": "+str(solution)
