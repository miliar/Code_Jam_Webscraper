#!/usr/bin/python3
key = {}
def setup():
	lines = []
	fh = open('setup.in')
	for line in fh:
		lines.append(line)
	fh.close()
	key['z'] = 'q'
	key['q'] = 'z'
	for j in range(3):
		for i in range(len(lines[j])):
			if lines[j][i] >= 'a' and lines[j][i] <= 'z':
				key[lines[j][i]] = lines[j+3][i]

def main():
	fh = open('A-small-attempt0.in')
	i = 0
	for line in fh:
		if i != 0:
			wine = line
			for j in range(len(line)):
				if line[j] >= 'a' and line[j] <= 'z':
					wine = wine[:j] + key[line[j]] + wine[j+1:]
			print('Case #' + str(i) + ':', wine, end='')
		i = i + 1

setup()
main()
#for k in key.keys():
#	print(k, key[k])




