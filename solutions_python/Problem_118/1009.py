input = open("C-small-attempt0.in","r")
output = open("output","w")
input.readline()

numbers = [1,4,9]
i = 1
extra = [""] + range(10)
while i < 100:
	for s in extra:
		n = int(str(i) + str(s) + str(i))
		if str(n**2) == str(n**2)[::-1]:
			numbers.append(n**2)
	i += 1
numbers.sort();
print numbers
n = 1
for line in input:
	a,b = map(int,line.strip().split())
	output.write("Case #{}: {}\n".format(n,len([i for i in numbers if i >= a and i <= b])))
	n += 1
input.close()
output.close()