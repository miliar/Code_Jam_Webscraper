import sys
input = open(sys.argv[1])
cleartext = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
ciphertext = ('y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q', ' ')
input.readline()
lines = 1
for line in input:
	s = ''
	for i in line.rstrip()[:]:
		s = s + cleartext[ciphertext.index(i)]
	print('Case #' + str(lines) + ': ' + s)
	lines += 1
input.close()
