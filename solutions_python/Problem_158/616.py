file = open("input")

counter_i = 1
counter_end_i = file.readline()


def solve(x,r,c):
	n=r*c
	if n==1 or n==3:
		if x==1:
			return 1
		else:
			return 0
	elif n==2 or n==4 or n==8:
		if x==1 or x==2:
			return 1
		else:
			return 0
	elif n==6:
		if x==4:
			return 0
		else:
			return 1
	elif n==9:
		if x==1 or x==3:
			return 1
		else:
			return 0
	elif n==12:
		return 1
	elif n==16:
		if x==3:
			return 0
		else:
			return 1
	

while (counter_i <= int(counter_end_i.strip())):
	current_line = file.readline().strip().split(' ')
	x=int(current_line[0])
	r=int(current_line[1])
	c=int(current_line[2])
	if solve(x,r,c):
		print "%s%d%s%s"%("Case #",counter_i,": ","GABRIEL")
	else:
		print "%s%d%s%s"%("Case #",counter_i,": ","RICHARD")

	counter_i=counter_i+1
