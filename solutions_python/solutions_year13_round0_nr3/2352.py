import math

f = open("C-small-attempt0.in")
lines = f.readlines()
f.close()

lines = map(lambda s:s.strip('\n'),lines)

T = lines[0]
cases = map(lambda l: l.split(" "),lines[1:])

res = []
count = 0

for i,case in enumerate(cases):
	a_range = range(int(case[0]),int(case[1])+1)
	count = 0

	for n in a_range:
		root = int(math.sqrt(n))
	
		if (root**2 == n) and (str(n)[::-1] == str(n)) and (str(root)[::-1] == str(root)):
			count += 1
	
	res.append("Case #{0}: {1}".format(i+1,count))

f = open("result.out","w")
f.write("\n".join(map(lambda x: str(x),res)))
f.close()



