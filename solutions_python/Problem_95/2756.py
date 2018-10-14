fin = open('A.in', 'r')
fout = open('A.out', 'w')
table = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def rin():
	return fin.readline().strip()

def solve():
	global table
	g_string = rin()
	if len(g_string) > 100:
		return 'ERROR. G has more than 100 chars'

	e_string = ''
	for letter in g_string:
		e_string += table[letter]
	return e_string

if __name__ == '__main__':
	T = int(rin())
	G = ''
	ans = ''
	for test_num in range(T):
		G = solve()
		ans = 'Case #%d: %s\n' %(test_num+1, G)
		fout.write(ans)
