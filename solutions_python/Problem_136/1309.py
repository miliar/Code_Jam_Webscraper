fopen = open('B-large.in')
fopen2 = open('Output.txt','w')
T = fopen.readline().strip()
T = int(T)
for num in range(1,T+1):
	sum = 0.0
	fac = 2.0
	line = fopen.readline().strip().split(" ")
	x = float(line.pop())
	f = float(line.pop())
	c = float(line.pop())
	ini = sum + (x/(fac))
	fin = sum + (c/(fac)) + (x/(fac+f))
	while ini > fin:
		sum += (c/(fac))
		fac += f
		ini = sum + (x/(fac))
		fin = sum + (c/(fac)) + (x/(fac+f))
	output="Case #" + str(num) + ": " + str(ini)
	fopen2.write(output+"\n")
fopen2.close()
fopen.close()