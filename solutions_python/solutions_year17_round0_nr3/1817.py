
def start(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	numTest = int(lines[0])
	stallMain(numTest, lines[1:])


def stallMain(numTest, inpts):
	output = open('stall_output.in', 'w')
	for i in xrange(numTest):

		res = stall(i, inpts[i])
		output.write(res + '\n')
	output.close()


def stall(case, inpt):
	numStalls, people = inpt.split(' ')
	numStalls = int(numStalls)
	people = int(people)
	stalls = [1] + ([0] * numStalls) + [1]
	#print stalls
	last_ls, last_rs = 0, 0
	max_m, min_m = 0, 0
	for each in xrange(people):
		stall_max = []
		stall_min = []

		for i in xrange(len(stalls)):
			if not stalls[i]:


				ls, rs = calc(i, stalls)

				stall_min.append([i, min(ls, rs), ls, max(ls, rs)])

		stall_min.sort(compare, reverse= True)

		stall_min_filtered = [x for x in stall_min if x[1] == stall_min[0][1]]
		if len(stall_min_filtered) == 1:
			m_stall = stall_min_filtered[0]
			stalls[m_stall[0]] = 1
			#print 'a'
			max_m, min_m = m_stall[3], m_stall[1]

		else:
			stall_min_filtered.sort(comparator, reverse = True)

			stall_min_filtered = [x for x in stall_min_filtered if x[3] == stall_min_filtered[0][3]]

			if len(stall_min_filtered) == 1:
				m_stall = stall_min_filtered[0]
				stalls[m_stall[0]] = 1
				max_m, min_m = m_stall[3], m_stall[1]
			else:

				stall_min_filtered.sort(compareLeft)
				m_stall = stall_min_filtered[0]
				stalls[m_stall[0]] = 1
				max_m, min_m = m_stall[3], m_stall[1]

	return "Case #" + str(case + 1) + ": " +  str(max_m) + ' ' + str(min_m)



def calc(i, stall):
	ls, rs  = 0, 0
	for x in xrange(i + 1, len(stall)):
		if stall[x] == 1:
			break
		else:
			rs += 1


	for x in xrange(i - 1, 0, -1):
		if stall[x] == 1:
			break
		else:
			ls += 1
	return [ls, rs]

def compareLeft(a, b):
	if a[2] > b[2]:
		return 1
	elif a[2] == b[2]:
		return 0
	else:
		return -1
	return 4	

def compare(a, b):
	if a[1] > b[1]:
		return 1
	elif a[1] == b[1]:
		return 0
	else:
		return -1

def comparator(a, b):
	if a[3] > b[3]:
		return 1
	elif a[3] == b[3]:
		return 0
	else:
		return -1



#stall(1000, 1)
start('C-small-1-attempt0.in')






