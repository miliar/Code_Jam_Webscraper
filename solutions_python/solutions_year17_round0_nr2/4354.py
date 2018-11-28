def do_work(a):

	digits = [int(i) for i in str(a) ]

        a = 0
        num = []
        appended = False
	for b in digits:
		if a > b:
                        num = num[:-1]
                        num.append(a-1)
                        num.append('9' * (len(digits)-len(num)))

                        break

		else:
			num.append(b)
		a = b	

	return int(''.join(map(str, num)))


def solve(a):
    new_a = a
    while True:
        new_a = do_work(a)
        #print new_a
        if new_a == a:
            break

        a = new_a

    return a





T = int(raw_input())

for case in xrange(1, T+1):
	N = int(raw_input())
	a = solve(N)
	print 'Case #%d: %s' % (case, a)