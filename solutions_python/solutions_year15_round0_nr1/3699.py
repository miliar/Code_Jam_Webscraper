import re, sys

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Insert an input file path'
		exit()
	with open(sys.argv[1], 'r') as data:
		data_size = data.readline()
		for i, d in enumerate(data):
			s_max, people = re.sub('\n', '', d).split(' ')
			p_tot = 0
			p_needed = 0
			if len(re.findall('0', people)) != 0:
				for s_i in xrange(len(people)):
					s_people = int(people[s_i])
					if p_tot > len(people):
						break
					if s_people != 0:
						if p_tot >= s_i: 
							p_tot += s_people
						else:
							p_needed += s_i - p_tot
							p_tot += p_needed + s_people
			print "Case #%d: %d" % (i + 1, p_needed)


