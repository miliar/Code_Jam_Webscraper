t = int(input())
for i in range(t):
	n = list(map(int, input()))
	
	#handle case with 1 digit
	if (len(n) == 1):
		print("Case #", i+1, ":", sep='', end=' ');
		print(int(''.join(map(str, n))))
	
	#handling case with multiple digits
	else:
		found = False
		size =len(n)
		while(not found):

			for j in range(size-1):
				j_ = j+1
				if (n[j] > n[j_]):
					n[j] -= 1
					n[j_:size] = [9] * (size - j_)
					break;

				else:
					j+=2

			if (j==size):
				print("Case #", i+1, ":", sep='', end=' ');
				print(int(''.join(map(str, n))))
				found = True