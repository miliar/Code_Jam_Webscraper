import math
PI=math.pi

for x in range(input()):
	r,t=[int (i) for i in raw_input().split(' ')]
	paint_left=t
	y=0
	rings=0
	while paint_left>=0:
		paint_left-=(2*r + (4*y+1))
		y+=1
		if paint_left>=0:
			rings+=1
	print "Case #"+str(x+1)+": "+str(rings)