import sys
import math


outfile = open("A.txt", "w")
infile = open("A-large.in", "r")

num_cases = int(infile.readline())

for k in range(1, num_cases + 1):
	triangles = 0
	line = infile.readline()
	temp = line.split()
	max_keys = int(temp[0])
	num_keys_avail = int(temp[1])
	num_letters = int(temp[2])
	temp = infile.readline().split()
	frequencies = []
	keys = [[] for num in range(0, num_keys_avail)]
	for freq in temp:
		frequencies.append(int(freq))
	frequencies.sort(reverse=True)
	reverse = False
	presses = 0
	first = True
	while len(frequencies) > 0:
		if first:
			for i in range(0, num_keys_avail):
				if len(frequencies) == 0:
					break
				freq = frequencies.pop(0)
				keys[i].append(freq)
				presses = presses + freq
			reverse = True
			first = False
			continue
		if reverse:
			for i in range(num_keys_avail-1, -1, -1):
				if len(frequencies) == 0:
					break
				freq = frequencies.pop(0)
				keys[i].append(freq)
				presses = presses + freq * len(keys[i])
			reverse = False
		else:
			for i in range(0, num_keys_avail):
				if len(frequencies) == 0:
					break
				freq = frequencies.pop(0)
				keys[i].append(freq)
				presses = presses + freq * len(keys[i])
			reverse = True
			
	outfile.write("Case #%s: %s\n" % (k, presses))
infile.close()
outfile.close()