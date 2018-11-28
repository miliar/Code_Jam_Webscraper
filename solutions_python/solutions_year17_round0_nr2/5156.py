
def tidy_number(i, n):

	
	str_n = str(n)
	n_array = [n]
	carry = False
	head = 0
	index = 0

	if (n > 9):# If single digit, already tidy.

		n_array = [0] * len(str_n)	

		for k in range(len(str_n)):
			
			n_array[k] = int(str_n[k])


		while(index < len(str_n)-1):			
				
			#print("i #{}: narray {}".format(index, str(n_array) ))

			if( n_array[index] < n_array[index+1] ):	
				head += 1		

			if( n_array[index] > n_array[index+1] ):

				if(not carry):
					n_array[head] = n_array[head]-1
					carry = True

				n_array[head+1] = 9			
				index = -1

			index += 1				
	
	output = int(''.join(map(str,n_array)))

	print("Case #{}: {}".format(i,  output) )	
	

t = int(input())

for i in range(1,t + 1):
	n = input()
	tidy_number(i,int(n))
	

