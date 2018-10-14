#read file
f = open('input.in', 'r')
lines = f.readlines()
f.close()
t = int(lines[0].split()[0])
opf = open('task.out', 'w')
for l in range(1,t+1):
	line =lines[l].split()
	c, f, x =  [float(item)  for item in line]
	#print 'values: ', c, f,x
	#actuall logic
	ir=2
	cr=ir
	till_now=0
	while(1):
		cr_time=x/cr+till_now
		nw_time=c/cr + x/(cr+f)+till_now
		if cr_time < nw_time:		 
			opf.write('Case #'+str(l)+': '+str(cr_time)+'\n')
			break
		till_now= till_now + c/cr
		cr=cr+f
		
opf.close()