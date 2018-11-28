file = open("B-small-attempt1.in", "r")
contains = file.read().split()
lines = int(contains[0])
numbers = contains[1 : lines+1]

output = open("B-small-attempt1.out", "w")

def form(result, length, m, j):
	if int(m) - 1 != 0:
		result += str(int(m) - 1) + "9" * (length - j) 
	else:
		result += "9" * (length - j)
	return result
	
results = []
for i in numbers:
	length = len(i)
	result = ""
	if length == 1:
		result = i
	else:	
		m = i[0]
		cnt = 1
		for j in range(1,length):
			n = i[j]
			if m == n and j + 1 < length:
				cnt += 1
				result += m
			elif m < n and j + 1 < length:
				result += m
				m = n
			elif m > n and cnt == j:
				result = form("", length, m, 1)
				break
			elif m > n:
				result = form(result, length, m, j)
				break
			else:
				result += m + n
	results.append(result)
	
	
for i in range(lines):
	output.write("Case #" + str(i + 1) + ": " + results[i] + "\n")