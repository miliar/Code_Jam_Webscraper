import sys

def main():
	ncas = int(sys.stdin.readline())
	for t in range(ncas):
		msg = sys.stdin.readline().strip()
		n = ''
		dic = []
		for i in msg:
			if i not in dic:
				dic.append(i)
			m = dic.index(i)
			if m >= 10:
				m = chr(ord('a') + m - 10)
			else:
				m = str(m)
			n = n + m
		res = ''
		for i in n:
			if i == '0':
				res += '1'
			elif i == '1':
				res += '0'
			else:
				res += i
		if len(dic) == 1:
			dic.append('0')
		#print msg, '|', n, '|', res, int(res, len(dic))
		print 'Case #%d: %d' % (t+1, int(res, len(dic)))

main()