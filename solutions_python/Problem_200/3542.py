n = int(input())
case = 1
while(n):
	integer = input()
	array = list(integer)
	size = len(array)
	if len(array) == 1:
		print("Case #", case, ": ", array[0], sep="")
	else:	
		for i in range (1, len(array)):
			if int(array[size-1]) < int(array[size-2]):
				array[size-1] = 9
				array[size-2] = int(array[size-2]) - 1
			size = size-1
		print("Case #", case, ": ",sep="",end="")	
		if array[0] != 0:
			print(array[0], end="")
		j = 1
		length = len(array) - 1
		while(length > 0 and array[j] != 9):
			print (array[j], end="")		
			j = j+1	
			length = length-1
		for j in range (0, length):
			print("9", end="")	
		
		print(" ")
	case = case +1	
	n = n-1	