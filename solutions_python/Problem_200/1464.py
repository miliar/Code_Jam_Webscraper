cases = []
def Order(n):
	i = 0
	no = n
	nos = str(no)
	digits = [int(s) for s in nos]
	digits = list(reversed(digits))
	# print(len(str(no)))
	# print(digits)
	while(i < len(str(no))-1):
		right = digits[i]
		# print(right)
		left = digits[i+1]
		# print(left)
		if left > right:
			# print(no%pow(10,i))
			no -= no%pow(10,i+1) +1
			# no += 
			# print(right * pow(10,i), i, len(str(no)))
			# no = Order(no)
			nos = str(no)
			i = 0
			# print(nos)
			digits = [int(s) for s in nos]
			# print(digits)
			digits = list(reversed(digits))
		i += 1
	# print(i)
	return no
	
	
with open("B-large.in", "r") as input:
	T = int(input.readline())
	for line in input:
		N = int(line)
		# print(N)
		# print(Order(N))
		cases.append(Order(N))
		
		
		
		
o = ""
for i in range(T):
	o += "Case #" + str(i+1) + ": " + str(cases[i]) + "\n"
# print(o)
	
with open("output.txt", "w") as output:
	output.write(o)
	