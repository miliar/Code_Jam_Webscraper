import sys

cypher = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

rl = lambda : sys.stdin.readline()

num_cases = int(rl())

for i in range(num_cases):
	plaintext = ''
	cyphertext = rl().strip()
	for char in cyphertext:
		plaintext += cypher[char]
	print('Case #' + str(i + 1) + ': ' + plaintext)
	
