import math
f_in = open("c:/In/D-small-attempt2.in",'r')
f_out = open("c:/In/D-small-attempt2.out",'w')
nlines = int(f_in.readline())
for i in range(nlines):
	gabriel = True
	xrc = map(lambda x: int(x), f_in.readline().split())
	if xrc[1] < xrc[2]:
		temp = xrc[2]
		xrc[2] = xrc[1]
		xrc[1] = temp
	nsquares = xrc[1]*xrc[2]
	ratio = float(nsquares)/xrc[0]
	if math.floor(ratio) != math.ceil(ratio):
		gabriel = False
	elif xrc[0] > 2:			
		if xrc[0] > xrc[1]:
			gabriel = False
		else:
			if xrc[2] == 1:
				gabriel = False
			if xrc[0] == 4:
				if xrc[2] == 2:
					gabriel = False				
	result = ""
	if gabriel:
		result = "GABRIEL"
	else:
		result = "RICHARD"
	f_out.write("Case #" + str(i + 1) + ": " + result + "\n")
f_in.close()
f_out.close()