f = file("test.txt", "r")
fout = file("output.txt", "w")
myString = ""

input = f.read().split("\n")
tests = int(input[0])
case = 1

def isRecycled(n, m):
	n = list(n)
	m = list(m)
	result = False
	i = 1
	while i < len(n) and not result:
		 m.insert(0, m.pop())
		 result = n == m and True
		 i += 1
	return result

while case <= tests:
	line 	= input[case].split(" ")
	start 	= int(line[0])
	end 	= int(line[1])
	counter = 0
	for i in range(start, end+1)[::-1]:
		for j in range(start, i):
			counter += isRecycled(str(j), str(i)) and 1
	
	myString += "Case #%d: %d\n" % (case, counter)
	case += 1


fout.write(myString)







