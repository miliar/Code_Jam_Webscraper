next_input = lambda:raw_input().strip()

def get_m():
	m = []
	for i in range(4):
		m.append( map( int, next_input().split(' ') ) )
	return m

def get_i():
	return int(next_input())

def get_r():
	ri1 = get_i()
	m1 = get_m()
	r1 = m1[ ri1 - 1 ]
	return r1

def case_i(i, ans):
	return 'Case #%d: %s' % (i+1, str(ans))

def main():
	n = get_i()
	for i in range(n):
		r1 = set(get_r())
		r2 = set(get_r())
		ans = r1 & r2
		if len(ans) == 1:
			print case_i(i, ans.pop())
		elif len(ans) > 1:
			print case_i(i, 'Bad magician!')
		elif len(ans) == 0:
			print case_i(i, 'Volunteer cheated!')


main()