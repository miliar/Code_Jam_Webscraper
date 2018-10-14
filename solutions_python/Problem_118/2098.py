import math
n = int(raw_input())
for k in range(n):
	a,b = map(int, raw_input().split())
	def is_palindrome(num):
		for i in range(len(num)/2):
			if num[i]!=num[len(num)-i-1]: return False
		return True
	cont=0
	for num in range(a,b+1):
		no = math.sqrt(num)
		if  no == math.trunc(no) and is_palindrome(str(num)) and is_palindrome(str(int(no))):
			cont+=1
	print "Case #"+str(k+1)+": "+ str(cont)

