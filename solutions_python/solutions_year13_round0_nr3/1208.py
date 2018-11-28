from __future__ import print_function
import sys

sys.stdin = open("C.in")
sys.stdout = open("C.out", "w")

T = int(raw_input())

for test in range(T):
	a, b = raw_input().split()
	
	lenA = len(a)
	lenB = len(b)
	
	a, b = map(int, (a,b))
	
	print("Case #%d: " % (test + 1), end = "")
	
	cool = lambda x: all((x[i] == x[-1 - i]) for i in range(len(x)))
	
	count = 0
	
	for left in [""] + range(1,10 ** (lenA//2 + 1)):
		try:
			whole = int( str(left) + str(left)[::-1] ) ** 2
		
			if (a <= whole <= b) and cool(str(whole)):
				count += 1
			elif whole > b:
				break
		except:
			pass
		
		for i in range(10):
			whole = int( str(left) + str(i) + str(left)[::-1] ) ** 2
			
			#print(whole ** 0.5)
			
			if (a <= whole <= b ) and cool(str(whole)):
				count += 1
	
	print(count)