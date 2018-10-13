#!/usr/bin/env python

import sys

if len(sys.argv) >= 2:
	input_filename = sys.argv[1]
else:
	print "Please specify an input file"
	exit()

def findCorrespondences(encoded, decoded):
	if len(encoded) is len(decoded):
		result = dict()
		for l in range(len(encoded)):
			enc_char, dec_char = encoded[l], decoded[l]
			if not result.has_key(enc_char):
				result[enc_char] = dec_char
		return result
	else:
		raise Exception("Stuff's borked")

def findCorrespondence(encoded, encoding):
	output = ""

	for l in range(len(encoded)):
		char = encoded[l]
		output += encoding[char]

	return output

examples = open("examples.txt")

lines = examples.readlines()

examples.close()

encoding_map = dict()

for n in range(3):
	encoded, decoded = lines[n].strip(), lines[n+3].strip()

	correspondences = findCorrespondences(lines[n], lines[n+3])
	encoding_map.update(correspondences)
	
challenge_input = open(input_filename)

lines = challenge_input.readlines()

challenge_input.close()

lines_num = int(lines.pop(0))

for n in range(lines_num):
	input_line = lines[n].strip()

	correspondence = findCorrespondence(input_line, encoding_map)

	print "Case #%d: %s"%(n + 1, correspondence)

