#Tidy Numbers

#counting back from N check tidy property

def isTidy(num):
	temp = num
	digits = []
	while temp != 0:
		digits.append(temp % 10)
		temp /= 10
	return list(reversed(sorted(digits)))==digits



def func():
	t = int(raw_input())
	for i in xrange(1, t+1):
		n = int(raw_input())
		while True:
			tidy = isTidy(n)
			if tidy:
				print "Case #{}: {}".format(i, n)
				break
			else:
				n -= 1


func()