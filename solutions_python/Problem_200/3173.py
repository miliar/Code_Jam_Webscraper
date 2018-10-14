def isTidy(s):
	last = '0'
	for ch in s:
		if ch >= last:
			last = ch
		else:
			return False;
	return True

def makeTidy(s, m):
	#print(s, m)
	if s == '':
		return (True, '' )
	ch = s[0]
	if (ord(ch) < ord(m)):
		return (False, '')

	b, st = makeTidy(s[1:], ch)
	if b:
		return (True, ch + st)
	else:
		if ch == '0' or ord(ch) - 1 < ord(m):
			return (False, '')
		else:
			return (True, (chr(ord(ch) - 1)) + '9'*(len(s) - 1))

def doTidy(s):
	b, st = makeTidy(s, s[0])
	if b:
		return st
	else:
		if ord(s[0]) > ord('1'):
			return chr(ord(s[0]) - 1) + '9' * (len(s) - 1)
		else:
			return '9' * (len(s) - 1)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = str(input())
  if isTidy(n):
	print("Case #{}: {}".format(i, n))
  else:
  	#print(n, doTidy(n))
  	x = doTidy(n)
  	print("Case #{}: {}".format(i, x))
