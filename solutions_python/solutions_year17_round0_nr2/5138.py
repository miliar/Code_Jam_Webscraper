
known_numbers = []

def tidy(number):
	str_repr = str(number)
	if len(str_repr) == 1:
		known_numbers.append(number)
		return True
	for i in range(1,len(str_repr)):
		if int(str_repr[i]) < int(str_repr[i-1]):
			return False
	known_numbers.append(number)
	return True

t = int(input())
for i in range(1, t + 1):
	number = int(input())
	for j in range(number,0,-1):
		if j in known_numbers:
			print("Case #{}: {}".format(i, j))
			break
		elif tidy(j) == True:
			print("Case #{}: {}".format(i, j))
			break