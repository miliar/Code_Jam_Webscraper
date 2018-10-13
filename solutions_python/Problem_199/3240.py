n = int(input())
case = 1
while(n):
	imp = 0
	count = 0
	string = input()
	pattern, size = string.split()
	array =  list(pattern)
	for i in range(0, len(array)-int(size) + 1):
		if array[i] == '-':
			count = count + 1
			temp = i
			for j in range(1, int(size)+1):
				if array[temp] == '-':
					array[temp] = '+'
				else:
				 	array[temp] = '-'	
				temp = temp + 1
	for k in range(len(array) - int(size), len(array)):
		if array[k] == '-':
			imp = 1
					
			
	if imp == 1:
		print ("Case #", case, ": IMPOSSIBLE", sep="")
	else:
		print ("Case #", case, ": ", count, sep="")			

	case = case + 1	
	n = n-1