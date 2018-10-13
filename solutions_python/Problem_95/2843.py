#!/usr/bin/python

input = [line.strip() for line in open('input.txt')]

alphabet = 		[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
googlerese = 	[' ', 'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q']

def googlereser():
	result = []
	for current in input:
		string = ''
		for character in current:
			if character in googlerese:
				string = string + alphabet[googlerese.index(character)]
		if len(string) > 0:
			if len(string) <= 100:
				result.append(string)
	return result

output = googlereser()
for i in range(len(output)):
	print 'Case #' + str(i+1) + ': ' + output[i]
