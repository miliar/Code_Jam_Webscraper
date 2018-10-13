d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def translate(text):
    result = ''
    for x in text:
	if x != "\n":
	    result += d[x]
    return result

f = open('sample', 'r')
fout = open('output', 'w')

n = int(f.readline())

for i in xrange(n):
    text = f.readline()
    output = 'Case #' + str(i+1) + ': ' + translate(text) + "\n"
    fout.write(output)

f.close()

