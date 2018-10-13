cases = int(raw_input())
pancackes = []
flippers = []
for i in xrange(cases):
	panckace, flipper = raw_input().split(' ')
	pancackes.append(panckace)
	flippers.append(int(flipper))

for i in xrange(cases):
	counter = 0
	flipper = flippers[i]
	pancacke = list(pancackes[i].strip('+'))

	#import pdb;pdb.set_trace()

	while len(pancacke) >= flipper:
		for j in xrange(flipper):
			if pancacke[j] == '+':
				pancacke[j] = '-'
			else:
				pancacke[j] = '+'
		pancacke = list("".join(pancacke).lstrip('+'))
		counter += 1


	if '-' in pancacke:
		print "Case #{0}: IMPOSSIBLE".format(i+1)
	else:
		print "Case #{0}: {1}".format(i+1, counter)

