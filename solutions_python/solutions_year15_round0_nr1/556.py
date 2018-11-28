# -*- coding: utf-8 -*-

import pdb

def min_friend_num(shyness_string):
	s = shyness_string.strip()
	s = s.rstrip('0')

	minimum_friend = 0
	current_clapping_num = 0
	for level in xrange(len(s)):
		if s[level] == '0':
			continue

		if level > current_clapping_num:
			minimum_friend += level - current_clapping_num
			current_clapping_num = level + int(s[level])
		else:
			current_clapping_num += int(s[level])

	return minimum_friend



def main():
	# pdb.set_trace()
	results = []

	with open('A-large.in.txt', 'r') as f:
		case_total = int(f.readline().strip())
		for i in range(case_total):
			line = f.readline().strip()
			if line != '':
				shyness = line.split()[1]
				results.append(min_friend_num(shyness))

	with open('out', 'w') as f:
		for i in range(len(results)):
			f.write('Case #{0}: {1}\n'.format(i+1, results[i]))	

if __name__ == '__main__':
	main()



