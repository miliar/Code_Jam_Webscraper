INPUT = 'A-large.in'
OUTPUT = 'mushroom1_large.txt'

with open(INPUT, 'r') as f:
	outputf = open(OUTPUT, 'w')
	for i, line in enumerate(f):
		if i == 0:
			current_case = 0
			continue
		elif i % 2 == 0:
			mushrooms = [int(x) for x in line.strip().split()]
			m2 = 0
			m1 = 0
			gm2 = 0
			m3 = 0
			for m_index, m_value in enumerate(mushrooms):
				if m_index == len(mushrooms) - 1:
					m2 = max((m2 - m_value), 0)
				else:	
					m2 += m_value
				if m_index > 0:
					m1 += max((mushrooms[m_index-1] - m_value), 0)
					gm2 = max(gm2, (mushrooms[m_index-1] - m_value))
			
			for m_index, m_value in enumerate(mushrooms):
				if m_index > 0:
					m3 += min(gm2, mushrooms[m_index-1])

					

			oline = 'Case #' + str(current_case) + ': ' + str(m1) + ' ' + str(m3) + '\n'	
			outputf.write(oline)	
		else:
			current_case += 1	
