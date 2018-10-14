from math import log10, factorial

sums = {2:1, 3:3, 4:6, 5:10, 6:15, 7:21}

try:
	nTests = int(raw_input())
	
	for test in xrange(1, nTests+1):
		A, B = [int(e) for e in raw_input().split()]
		#print A, B
		
		arr = [0] * (B+1)
		nDigits = int(log10(B))+1
		mult = 10 ** (nDigits-1)
		count = 0
		#print nDigits, mult
		
		for num in xrange(A, B+1):
			n = num
			temp = 0
			while not arr[n]:
				#if n != num:
				#	print num, n
				arr[n] = 1
				temp += 1
				last = 0
				while last == 0 or n < A or n > B:
					last = n % 10
					n = last * mult + n / 10
			if temp > 1:
				count += sums[temp]
			
			#if num == 122:
			#print "[%d, %d] num: %d, temp: %d, count: %d" % (A, B, num, temp, count)
			#	print arr
		#print arr
		print "Case #%d: %d" % (test, count)

except EOFError:
	pass
