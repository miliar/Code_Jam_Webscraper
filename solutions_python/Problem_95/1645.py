substitution_map = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q':'z'}
tests = int(raw_input())

for i in xrange(0, tests):
	phrase = raw_input()
	phrase2 = ""
	for j in xrange(0, len(phrase)):
		phrase2 += substitution_map[phrase[j]]
	print "Case #%d: %s" % (i+1, phrase2)
	
