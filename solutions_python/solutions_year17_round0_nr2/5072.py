# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# t = int(input())  # read a line with a single integer
# ans = 0
# arr = [100,132,1000,7,834,652,175,702,840,678,328,325,308,240,5,689,690,754,999,812,495,467,311,441,989,128,753,877,685,984,630,271,512,313,538,879,724,277,468,1,716,275,705,693,346,557,279,138,760,504,353,977,939,894,119,810,611,341,356,39,488,154,50,196,289,41,149,704,108,299,394,622,692,143,907,940,618,765,107,178,81,145,359,321,679,903,609,295,963,21,993,473,425,770,433,827,835,312,426,777,381]
arr = [str(s) for s in input().split(" ")]
for x in range( 1, int(arr[0])+1 ):
	k = arr[x]
	z = [i for i in str(k)]
	if '0' in z:
		while '0' in z:
			# print(''.join(z))
			for i in range(0,len(z)-1):
				if(z[i] > z[i+1]):
					z[i] = str(int(z[i]) - 1)
					for n in range(i+1,len(z)):
						z[n] = str(9)
			if z[0] == '0':
				break
		ans = int(''.join(z))
	else:
		while (all(earlier <= later for earlier, later in zip(z, z[1:]))) == False:
			for i in range(0,len(z)-1):
						if(z[i]>z[i+1]):
							z[i] = str(int(z[i]) - 1)
							for n in range(i+1,len(z)):
								z[n] = str(9)
		ans = int(''.join(z))
	print("Case #{}: {}".format(x, ans))
