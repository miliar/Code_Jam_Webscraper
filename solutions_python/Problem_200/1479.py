# Woooo! Trying the (not-that-) new hammer (python, that is) on ALL THE NAILZ!



tc = int(input())  # of test cases
for cc in range(1, tc + 1):
	n = list(input())

	di = 0 # deltaindex, ooo

	for i, c in enumerate(n):
		#print(di, i, n, c)
		if (i+1) < len(n):
			if int(c) < int(n[i+1]):
				di = i+1
			if int(c) > int(n[i+1]):
				n[di] = str(int(n[di])-1) # invariant: not zero
				#print(n)
				for z in range(di+1, len(n)):
					n[z] = '9'
				break



	n = ''.join(n)
	n = int(n)

	print("Case #{}: {}".format(cc, n))