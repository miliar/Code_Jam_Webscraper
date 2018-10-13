import math
if __name__=="__main__":
	file = open("B-large.in","r")
	items = int(file.readline())
	count = 1
	for item in range(0,items):
		_c,_f,_x = map(float,file.readline().split(' '))	
		_b = int(max(0, math.ceil(((_x-_c)/_c) - (2/_f))))
		time = 0.0
		for iter in range(0,_b):
			time += _c/(2+(iter * _f))
		time += _x/(2+(_b*_f))
		print "Case #"+str(count)+": "+str(time)
		count += 1
