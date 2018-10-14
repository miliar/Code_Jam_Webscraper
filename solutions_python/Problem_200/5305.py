t = int(raw_input())

def checkTidy(x):
	str_x = str(x)
	
	for i in range(len(str_x) - 1):
		if int(str_x[i]) > int(str_x[i + 1]):
			return False
	
	return True
	
def getTidy(n):
	while n > 9:
		if checkTidy(n):
			return n
		
		n = n - 1
	
	return n
	
	
for i in range(t):
	n = long(raw_input())
	print("Case #" + str(i + 1) + ": " + str(getTidy(n)))
