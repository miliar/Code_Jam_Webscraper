import math

f = file("A-small-practice.in")



def read_game(f):
	N, M = f.readline().strip().split(" ")
	N = long(N)
	M = long(M)
	return N, M

def is_palindrome(x):
	tmp = str(x)
	r = []
	for c in tmp:
		r.append(c)
	r.reverse()
	y = long("".join(r))
	return x == y

def is_square(x):
	root = math.sqrt(x)
	if root == long(root):
		return is_palindrome(long(root))
	return False

def check(start, end):
	size = 0
	for i in range(start, end+1):
		if is_palindrome(i):
			if is_square(i):
				size += 1
	return str(size)


game_count = int(f.readline())
for i in range(1, game_count + 1):
	N, M = read_game(f)
	result = check(N, M)
	print "Case #%d: %s" % (i, result)

f.close()