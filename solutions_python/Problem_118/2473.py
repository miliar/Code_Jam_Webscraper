import sys

from math import sqrt, floor

n = int(raw_input())

for ii in range(1, n + 1):
	inp = raw_input()
	(a, b) = map(long, inp.split(' '))

	count = 0
	i = long(floor(sqrt(a)))
	num = i * i

	if num < a:
		i += 1
		num = i * i

	while num <= b:
		palindrome = True
		palindrome_i = True

		str_i = str(i)
		str_num = str(num)

		l = len(str_num)
		l_i = len(str_i)
		
		for j in range(0, l_i / 2):
			if str_i[j] != str_i[l_i - j - 1]:
				palindrome_i = False
				break

		if palindrome_i:
			for j in range(0, l / 2):
				if str_num[j] != str_num[l - j - 1]:
					palindrome = False
					break
			

			if palindrome and palindrome_i:
				#print "%s and %s is palindrome" % (str_num, i)
				count += 1
		
		i += 1
		num = i * i

	print "Case #%s: %s" % (ii, count)
