input = open('./input', 'r')
output = open('./output', 'w')
line = input.readline()
n = int(line[:-1])
w=0
for x in range(n):
	line = input.readline();
	linea = line[:-1].split()
	n=int(linea[0])
	b=int(linea[1])
	m=int(linea[2])
	a=linea[3:]
	min = 30
	if b==0:
        	if m<=1:
                	min = m
        	else:
                	min = m+(2*(m-1))
	else:
        	if m<=2:
                	min = m
        	else:
                	min = m+(2*(m-2))
	y=0
	for z in a:
		z = int(z)
        	if b==0:
                	if z>=min:
                        	y=y+1
			else:
				y=y
        	else:
                	if z>=(min+2):
                        	y=y+1
                	elif z>=min:
                        	y=y+1
                        	b=b-1
                        	if b==0:
                                	min=min+2
	output.write('Case #'+str(w+1)+': '+str(y)+'\n')
	w=w+1
