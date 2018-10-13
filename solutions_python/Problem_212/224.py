
f = open('atiny.in')
fout = open('atiny.out', 'w')
f = open('asmall.in')
fout = open('asmall.out', 'w')
# f = open('alarge.in')
# fout = open('alarge.out', 'w')

numCases = int(f.readline().strip())



for numCase in range(numCases):
	print 'Case {}'.format(numCase + 1)

	ss = f.readline().strip().split(' ')
	N = int(ss[0])
	P = int(ss[1])

	groups = [int(a) % P for a in f.readline().strip().split(' ')]

	ret = 0
	ret = groups.count(0)
	if P == 2:
		print ret
		if 1 in groups:
			ret += groups.count(1) / 2
			if groups.count(1) % 2 == 1:
				ret += 1
		print ret
	elif P == 3:
		num1 = groups.count(1)
		num2 = groups.count(2)
		m = min(num1, num2)

		ret += m
		num1 -= m
		num2 -= m
		print ret

		ret += num1 / 3
		ret += num2 / 3
		num1 -= num1 / 3 * 3
		num2 -= num2 / 3 * 3
		print ret

		if num1 > 0 or num2 > 0:
			ret += 1
	elif P == 4:
		pass
	else:
		raise ValueError("{}".format(P))



	fout.write('Case #{}: '.format(numCase + 1))
	fout.write('{}\n'.format(ret))


fout.close()

"""

Input 
 	
Output 
 
3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1

Case #1: 3
Case #2: 4
Case #3: 1



"""

