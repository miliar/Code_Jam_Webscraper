if __name__ == '__main__':
	cases = int(raw_input())
	mapping = {'a': 'y', ' ': ' ', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q':'z','p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','z':'q'}
	solution = []
	for i in range(0,cases):
		i = 0
		jumbled = raw_input()
		string = ''
		for letter in jumbled:
			string += mapping[letter]
		solution.append(string)
	for i in range(0, cases):
		print 'Case #%d: %s'%(i+1,solution[i])
