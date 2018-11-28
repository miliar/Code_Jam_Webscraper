import string

f = open('A-small-attempt0.in', 'r')
g = open('output.txt', 'w')

mapping = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q', ' ' : ' ', '\n' : '\n'}

n = int(f.readline())
count = 1

while count <= n:
	line = f.readline()
	output = ''
	
	for letter in line:
		output += mapping[letter]
		
	g.write("Case #" + str(count) + ": " + output)

	count += 1
	
f.close()
g.close()