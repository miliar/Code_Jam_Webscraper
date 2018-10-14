
def tidy(n):
	t = n
	l = len(str(t))

	i = 0
	counter = 0

	while i < l:
		dig = t / pow(10,i) % 10
		digl = t / pow(10,i+1) % 10

		counter += dig * pow(10,i)

		if dig < digl:
			t -= counter + 1
			i = 0
			counter = 0
		else:
			i += 1

	return t

def is_tidy(n):
	for i in range(0,len(str(n))):
		if (n / pow(10,i) % 10) < (n / pow(10,i+1) % 10):
			return False
	return True

def brute_tidy(n):
	for i in range(0,n):
		if is_tidy(n - i):
			return n-i



lines = int(raw_input())

for i in range(lines):
	n = int(raw_input())
	t = tidy(n)

	print("Case #" + str(i+1) + ": " + str(t))
