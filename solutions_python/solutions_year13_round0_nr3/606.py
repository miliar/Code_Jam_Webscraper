from sys import *
from math import *


def palindr(a):
	a = str(a)
	for i in range(len(a)):
		if (a[i] != a[len(a) - i - 1]):
			return False
	return True
	
	
def next(a):      
	a = str(a)       
	if (a[0] == '2'):
		if (a[len(a) // 2] == '0' and len(a) % 2 == 1):
			a = a[:len(a) // 2] + '1' + a[len(a) // 2 + 1:]
			#a[len(a) // 2] = '1'
			a = int(a)
			return a
		else:
			b = 1
			for i in range(len(a)):
				b *= 10
			b += 1
			return b	
	else:
		if (len(a) % 2 == 1 and a[len(a) // 2] == '1'):
			#print(a)
			a = a[:len(a) // 2] + '2' + a[len(a) // 2 + 1:]
			#print(a)
			#a[len(a) // 2] = '2'
			if (palindr(int(a) * int(a))):
				return a
			a = a[:len(a) // 2] + '1' + a[len(a) // 2 + 1:]

			#a[len(a) // 2] = '0'
		for k in range(len(a) // 2):
			i = len(a) // 2 - k
			if (a[i] == '0'):
				#print(a)
				#print(i)  
				#print(a[:i])
				a = a[:i] + '1' + a[i + 1:]
				#a[i] = '1'
			
				a = a[:len(a) - i - 1] + '1' + a[len(a) - i:]
				#print(a)
				#a[len(a) - i - 1] = '1'
				for j in range(len(a) // 2 - i - 1):
					a = a[:j + i + 1] + '0' + a[j + i + 2:]
					#print(a)
					a = a[:len(a) - j - i - 2] + '0' + a[len(a) - j - i - 1:]
					#print(a)
					#exit()
					#a[j + i + 1] = a[len(a) - j - i] = '0'
				if (len(a) % 2 == 1 and i != len(a) // 2):
					a = a[:len(a) // 2] + '0' + a[len(a) // 2 + 1:]
				return a

		a = '2' + '0'* (len(a) - 2) + '2'
		#print(a)               
		#exit()
		return a
				
				 
fin = open("fair.in", "r")
fout = open("fair.out", "w")
t = int(fin.readline())
for q in range(t):
	ans = 0
	a, b = map(int, fin.readline().split())
	if (a <= 1 and b >= 1):
		ans += 1
	if (a <= 4 and b >= 4):
		ans += 1
	if (a <= 9 and b >= 9):
		ans += 1
	a = sqrt(a)
	b = sqrt(b)
	x = 10
	while (10 * x + 1 < a):
		x *= 10
	x += 1  
	while (x <= b):
		if (x >= a and palindr(x) and palindr(x * x)):
			ans += 1
			#if (q == 44):
			#	print(x, a)
			#print(x)
			#fout.write(str(x) + '\n')
		x = int(next(x))
		#if (not palindr(x) or not palindr(x * x)):
			#print(x, x * x)
		#if (ans % 1000 == 0):
		#	print(ans, len(str(x * x)))
		#print(a, b, x) 
	fout.write("Case #" + str(q + 1) + ": " + str(ans) + "\n")			

	