import math
def xor(x, y): return x ^ y
def add(x, y): return x + y
def solve_case(case):
	i = 1;
	bitmax = (1 << len(case)) - 1
	pos = []
	while(i < bitmax):
		if i > (~i & bitmax):
			i += 1
			continue
		x = i
		arr1 = []
		arr2 = []
		cur = 0
		while x != 0:
			lowest = x & -x
			while cur < int(math.log(lowest, 2)):
				arr1.append(case[cur])
				cur += 1;
			arr2.append(case[cur])
			cur += 1;
			x &=  ~lowest
			
		arr1.extend(case[cur:])
		if(len(arr1) == 0 or len(arr2) == 0):
			print i
			print case
			print arr1, arr2
			exit()
		if(reduce(xor, arr1) == reduce(xor,arr2)):
			pos.append(max(reduce(add, arr1), reduce(add,arr2)))
		i += 1
		
	if len(pos) == 0:
		return "NO"
	else:
		return str(max(pos))
			

fin = open('input11.txt')
fout = open('out11.txt','w')

inp = fin.readlines()
tot_case = int(inp[0])
for i in range(1, tot_case+1):
	in_case = [int(x) for x in inp[2 * i].split(' ')]
	fout.write("Case #" + str(i) + ": " + solve_case(in_case) + "\n")
	
fin.close()
fout.close()