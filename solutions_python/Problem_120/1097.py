import math

f = open("bullseye.txt",'r')
prompt = f.readlines()[1:]
count = 0
for a in prompt:
	a = a.replace('\n','').split()
	radius = int(a[0])
	m_L = int(a[1])
	num_iter = 0
	fill_mL = 0
	while(fill_mL <= m_L):
		num_iter += 1
		fill_mL += (radius + (2*num_iter-1))**2 - (radius + (2*num_iter-2))**2
	count += 1
	print "Case #" + str(count) + ": " + str(num_iter-1)
