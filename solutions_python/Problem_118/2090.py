import math

def palindrome(num):
	if round(num) == num:
		num = int(num)
	n = num
 	rev = 0
 	while num > 0:
	  dig = num % 10
	  rev = rev * 10 + dig
	  num = num / 10

 	if n == rev:
	  return True
	else: 
	  return False

f = open('C-small-attempt0.bin', 'r')
x = int(f.readline())

for i in range(1, x + 1):
	out = 0

	y = f.readline().replace('\n', '').split(' ')
	l = int(y[0])
	u = int(y[-1])

	for num in range(l, u + 1):
		if palindrome(num) and palindrome(math.sqrt(num)):
			out += 1
	print 'Case #' +str(i)+ ': ' + str(out)