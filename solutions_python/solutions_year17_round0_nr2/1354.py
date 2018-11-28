
def nine(l, at, to):
	for i in range(at, to):
		l[i] = 9
	
t = int(input())
for case_number in range(1, t + 1):
	n_s = input()
	
	l = [int(i) for i in n_s]
	
	result = 0
	
	nines_start = len(l)
	
	for i in range(len(l) - 1, 0, -1):
		if(l[i] < l[i - 1]):
			nine(l, i, nines_start)
			nines_start = i
			l[i - 1] -= 1
	
	result = ""
	if l[0] != 0:
		result += str(l[0])
	for i in range(1, len(l)):
		result += str(l[i])
	
	print("Case #{}: {}".format(case_number, result))
	


