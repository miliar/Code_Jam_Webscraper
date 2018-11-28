#gc1
import string

file = open('A-small-attempt0.in')

if __name__ == '__main__':
	n_tests = int(file.readline().replace('\n',''))
	
	for k in range(n_tests):
		f_choice = int(file.readline().replace('\n',''))
		grid_1 = []
		possibilities = [0,0,0,0]
		for i in range(4):
			row = file.readline().replace('\n','').split(' ')
			grid_1.append([])
			for l, j in enumerate(row):
				parameter = int(j)
				if (i+1) == f_choice:
					possibilities[l] = parameter
				grid_1[i].append(int(j))
		
		
		choices = []
		grid_2 = []
		s_choice = int(file.readline().replace('\n',''))
		for i in range(4):
			row = file.readline().replace('\n','').split(' ')
			grid_2.append([])
			for l, j in enumerate(row):
				parameter = int(j)
				if (i+1) == s_choice:
					if parameter in possibilities:
						choices.append(parameter)
				grid_2[i].append(int(j))
		
		
		if len(choices) == 0:
			print "Case #%d: Volunteer cheated!" % (k+1,)
		elif len(choices) == 1:
			print "Case #%d: %d" % (k+1, choices[0])
		else:
			print "Case #%d: Bad magician!" % (k+1,)
		
			
	