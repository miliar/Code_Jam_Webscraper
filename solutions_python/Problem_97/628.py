#!/usr/bin/python
#
# stjepan.henc@fer.hr
#

T = int(input())


for i in range(T):
	ulaz = input().split(' ')
	
	a = int(ulaz[0])
	b = int(ulaz[1])
	
	tot = 0
	
	for n in range(a, b + 1):
		s = str(n)
		for j in range(1, len(s)):
			novi = s[j:len(s)] + s[0:j]
			
			if novi == s:
				break
			
			if novi[0] != '0' and int(novi) >= a and int(novi) <= b:
				tot += 1 
	
	
	print("Case #" + str(i + 1) + ":", round(tot / 2))	
