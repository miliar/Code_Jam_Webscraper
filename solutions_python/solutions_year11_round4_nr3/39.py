import sys

def gcd(a,b):
	while b != 0:
		a, b = b, a % b
	return a


def factors(n):  
	fact = []  
	check = 2  
	while check <= n:  
		if n % check == 0:  
			fact.append(check)  
			while (n % check == 0):
				n = n / check
		check += 1  

	return fact

rl = lambda: sys.stdin.readline().strip()

t = int(rl())
for case_number in range(t):
	n = int(rl())
	price = 0
	calls1 = 0
	i = 1
	facts = set()
	while i <= n:
		if (price == 0) or (price % i != 0):
			calls1 += 1
			if price == 0:
				price = i
			else:
				price = (price * i) / gcd(price, i)

		factors_list = factors(i)
		for factor in factors_list:
			if not(factor in facts):
				facts.add(factor)

		i += 1

	price = 0
	calls2 = 0
	i = n
	while i > 0:
		if (price == 0) or (price % i != 0):
			calls2 += 1
			if price == 0:
				price = i
			else:
				price = (price * i) / gcd(price, i)

		i -= 1
	result = calls1 - len(facts)
	if n == 1:
		result = 0

	print "Case #%d: %d" % (case_number + 1, result)

