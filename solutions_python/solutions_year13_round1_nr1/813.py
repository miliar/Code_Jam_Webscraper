import math
f = open("test")
file = f.read()
f.close()
result = []
input = file.split("\n")
print input
for temp in input[1:-1]:
	temp1 = temp.split(" ")
	r = int(temp1[0])
	t = int(temp1[1])
 
	used = 0
	total = 0
	while used < t:
		used += ((r+1)**2 - r**2)
		r += 2
		if used > t:
			break
		total += 1
	result.append(total)

finalfile = open("result",'w')

nub = 1
for k in result:
	finalfile.write("Case #%d: %d\n"%(nub,k))
	nub += 1
print result
