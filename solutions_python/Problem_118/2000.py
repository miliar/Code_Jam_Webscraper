from math import sqrt
# ------------------------------------------------------------------------------
# globals
# ------------------------------------------------------------------------------
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def ispalindrome(v):
	if v[::-1] == v:
		return True
	return False

def is_square_of_palindrome(v):
	v = int(v)
	sv = 0
	if v == 1:
		return True
	if is_square(v):
		sv = int(sqrt(v))
		if ispalindrome(str(sv)):
			return True
	return False
# ------------------------------------------------------------------------------
# solution
# ------------------------------------------------------------------------------

f = open('in')
fo = open('out', 'w')

for T in range(int(f.readline())):
	pcount = 0
	endpoints = map(int, f.readline().strip().split())
	v = map(str,range(endpoints[0], endpoints[1]+1))

	for i in range(len(v)):
		# 1 Check palindrome
		if ispalindrome(v[i]):
			if is_square_of_palindrome(v[i]):
				pcount = pcount + 1

	print 'Case #%d: %s' % (T+1, pcount)
	fo.write('Case #%d: %s\n' % (T+1, pcount))


fo.close()
f.close()
