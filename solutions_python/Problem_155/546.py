f = open('A-large.in','r')
o = open('ovation.out', 'w')

N = int(f.readline().strip('\n'))
cases = [x.strip('\n').split(' ') for x in f.readlines()]

def friends(max_shyness, audience):
	"""finds how many additional friends are needed

	length - max shyness of audience
	audience - # of audience of each shy-level from 0 to max_shyness
	"""
	currently_standing = 0
	audience_needed = 0
	for i in range(max_shyness+1):
		if currently_standing < i:
			audience_needed += 1
			currently_standing = i
		currently_standing += int(audience[i])
	return audience_needed


for i in range(N):
	case = cases[i]
	o.write('Case #' + str(i+1) + ': ' + str(friends(int(case[0]), case[1])) + '\n')