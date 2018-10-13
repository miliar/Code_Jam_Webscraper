import string
def solve(data):
	dictionary = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z':'q', 'q':'z'}
	
	result = ""
	for ch in data:
		if ch in dictionary:
			result += dictionary[ch]
		else:
			result += ch
	return result

if __name__ == '__main__':
	import sys
	N = int(sys.stdin.readline())
	for i in xrange(N):
		input_str = sys.stdin.readline().strip()
		res = solve(input_str)
		print "Case #%d: %s" % (i + 1, res)	

