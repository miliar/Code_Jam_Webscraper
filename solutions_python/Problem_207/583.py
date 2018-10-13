def color(i):
	if(i==1): return "R"
	if(i==2): return "O"
	if(i==3): return "Y"
	if(i==4): return "G"
	if(i==5): return "B"
	
	return " color doesnt exist !!!!!!!!!!"




f = open('input.txt')

T = int(f.readline())

for case in range(1,T+1):
	line = [int(x) for x in f.readline().split(" ")]
	x,y,z = line[1], line[3], line[5]
	cx,cy,cz = "R", "Y", "B"

	if(x>y): 
		x,y=y,x 
		cx,cy=cy,cx
	if(x>z): 
		x,z=z,x 
		cx,cz=cz,cx
	if(y>z): 
		y,z=z,y 
		cy,cz=cz,cy

	if(x+y<z) :
		print("Case #"+str(case)+": "+"IMPOSSIBLE")
	else :
		ret=""
		equ = False
		if(x==y and y==z) : equ = True
		while(x+y+z>0):
			if(equ) : 
				ret = ret+cz+cy+cx
				z=z-1
				y=y-1
				x=x-1
			else : 
				ret = ret+cz+cy
				z=z-1
				y=y-1
				if(x==y and y==z) : equ = True
				else :
					if(x>y) : 
						x,y=y,x 
						cx,cy=cy,cx

		print("Case #"+str(case)+": "+ ret)






