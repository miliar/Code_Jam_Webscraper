file = open('170408b_out0.txt', 'w')
def printp(*args, **kwargs):
	kwargs['file'] = file
	print('Case #{}:'.format(_+1), *args, **kwargs)
for _ in range(int(input())):
	n = input()
	l = 0
	for i in range(1, len(n)):
		if n[i] < n[l]:
			printp((n[:l] + str(int(n[l])-1)).ljust(len(n), '9').lstrip('0'))
			break
		elif n[i] > n[l]:
			l = i
	else:
		printp(n)