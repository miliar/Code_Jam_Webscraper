def accurateQ(n):
	if len(str(n)) == 1:
		return True
	else:
		for i in range(1, len(str(n))): 
			if int(str(n)[i]) < int(str(n)[i - 1]):
				return False
	return True

n = int(input())

while not(accurateQ(n)):
	n -= 1

print(n)