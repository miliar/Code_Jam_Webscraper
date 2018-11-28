import re, sys
# there is only two possibilities after learning from the example :)
key1 = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

key2 = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

key = key1

def pprint(result):
	output = []
	for x in range(len(result)):
		output.append("Case #%d: %s" % (x + 1, result[x]))
	print '\n'.join(output)

def decode(input):
	return re.sub('(.)', lambda x: key[x.group(1)], input)

def parse(input):
	input = input.split('\n')
	number_of_case = int(input[0])
	g = []
	for i in range(number_of_case):
		g.append(input[1 + i])
	return g

def main():
	filename =  sys.argv[1]
	g = parse(open(filename).read())
	r = map(decode, g)
	pprint(r)

main()
	
