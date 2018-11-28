import math
inp = open("input.txt", 'r')

tests =int( inp.readline())

for i in range(tests):
	p = inp.readline().split('/')
	num =int( p[0])
	den = int(p[1])
	for j in range(9,-1,-1):
		if num>2**j:
			num = 2**j
			break
	if den%num == 0:
		den = den//num
		num = 1
	if num> den//2:
		den = den//2
	while num%2==0 and den%2==0:
		num = num//2
		den= den//2

	ans = math.log(den, 2)
	if ans%1==0:
		ans = int(ans)
	else:
		ans = 'impossible'
	print("Case #", i+1, ": ", ans, sep='')

		
