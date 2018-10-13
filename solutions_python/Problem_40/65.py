
import string
NUMS = string.digits + '.'

def remove_pa(s, ch):
	#print 'remove_pa', s, ch
	s = s[s.find(ch)+1:]
	#print 'return', s
	return s

def remove_num(s):
	s = s.lstrip()
	n = ''
	#print 'remove_num', s
	for i in xrange(len(s)):
		if s[i] in NUMS:
			n += s[i]
		else:
			return float(n), s[i:].lstrip()

def remove_name(s):
	name = ''
	for i in xrange(len(s)):
		if s[i] in string.lowercase:
			name += s[i]
		else:
			return name, s[i:].lstrip()

def parse(tree, s):
	# find '('
	dic = {}
	s = remove_pa(s, '(')
	# find digit
	digit, s = remove_num(s)
	dic['num'] = digit

	if s[0] == ')':
		dic['leaf'] = True
	else:
		dic['leaf'] = False
		dic['name'], s = remove_name(s)
		dic['left'], s = parse(tree, s)
		dic['right'], s = parse(tree, s)
	
	# find ')'
	s = remove_pa(s, ')')

	return dic, s

def solve():
	tree = {}
	lines = int(raw_input())
	s = ' '.join([raw_input() for i in xrange(lines)])
	d, s = parse(tree, s)

	lines = int(raw_input())
	for i in xrange(lines):
		node = d
		value = 1.0
		names = raw_input().split()[2:]
		value *= node['num']
		while True:
			#print '$', node['num']
			if not node['leaf']:
				if node['name'] in names:
					node = node['left']
				else:
					node = node['right']
				value *= node['num']
			if node['leaf']:
				break
		print '%.7f' % (value)

def main():
	cases = int(raw_input())
	for i in xrange(cases):
		print 'Case #%s:' % (i + 1)
		solve()

if __name__ == '__main__':
	main()