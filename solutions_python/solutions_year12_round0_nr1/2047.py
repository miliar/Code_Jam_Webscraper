google = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l',
 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', '\n': '\n', 'z' : 'q'}

inputs = open("""C:\\Users\\David\\Downloads\\A-small-attempt2.in""").readlines()[1:]

count = 1
for line in inputs:#inputs.split('\n'):
	outline = ("".join([google[i] for i in line]))
	print "Case #" + str(count) + ": "+ outline,
	count += 1