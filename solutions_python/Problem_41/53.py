
def solve(num):
	pos = length = len(num)
	for i in xrange(length - 1, 0, -1):
		#print num[i], num[i-1]
		if num[i] > num[i - 1]:
			pos = i - 1
			break

	#print pos
	for i in xrange(length - 1, 0, -1):
		if num[i] > num[pos]:
			#print num[i], num[pos]
			num[i], num[pos] = num[pos], num[i]
			#print num[i], num[pos]
			break
	s = ''.join(num[:pos+1]) + ''.join(reversed(num[pos+1:]))
	for i in xrange(len(s)):
		if s[i] != '0':
			return s[i:]

def main():
	cases = int(raw_input())
	for i in xrange(cases):
		print 'Case #%s: %s' % (i + 1, solve(list('0' + raw_input())))

if __name__ == '__main__':
	main()