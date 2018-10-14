__author__ = 'Rakshak.R.Hegde'
"""
Created on Apr 11 2015 AM 09:35

@author: Rakshak.R.Hegde
"""


def gline():
	return fi.readline().strip()


fi = open('A-small-attempt1.in')
fo = open('A-small-attempt1.out', 'w')
for t in range(1, int(gline()) + 1):
	count = gline().split()[1]
	sum = noF = 0
	for i, ch in enumerate(count):
		if sum < i:
			noF += i - sum
			sum = i
		sum += int(ch)
	fo.write('Case #{}: {}\n'.format(t, noF))
fo.close()