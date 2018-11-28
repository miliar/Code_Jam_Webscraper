import math
t = input()
for i in range(t):
	result = 0
	a,b = map(int, raw_input().split())
	x = math.sqrt(a)
	j = int(x)
	if x != j:
		j = j+1
	while j*j <= b:
		string = str(j*j) 
		if string == string[::-1]:
			string = str(j)
			if string == string[::-1]:
				result = result + 1
		j = j+1   

	print 'Case #{0}: {1}'.format(i+1,result)					
