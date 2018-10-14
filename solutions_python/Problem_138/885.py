import fileinput

def process(case_no, number, naomi_blocks, ken_blocks):
	naomi_blocks.sort()
	naomi_blocks_backup = naomi_blocks[:]
	ken_blocks.sort()
	ken_blocks_backup = ken_blocks[:]
	point_deceitful_war = 0
	point_war = 0
	
	while naomi_blocks:
		if naomi_blocks[0] < ken_blocks[0]:
			naomi_blocks.pop(0)
			ken_blocks.pop()
		else:
			naomi_blocks.pop(0)
			ken_blocks.pop(0)
			point_deceitful_war += 1

	naomi_blocks = naomi_blocks_backup
	ken_blocks = ken_blocks_backup
	
	while naomi_blocks:
		naomi_mass = naomi_blocks.pop(0)
		ken_len = len(ken_blocks)
		for idx in range(ken_len):
			if naomi_mass < ken_blocks[idx]:
				ken_blocks.pop(idx)
				break
		if len(ken_blocks) == ken_len:
			point_war = ken_len
			break
			
	print 'Case #%d: %d %d' % (case_no, point_deceitful_war, point_war)

indata = [line for line in fileinput.input()]
line_no = 1
for case_no in range(1, int(indata[0])+1):
	number = int(indata[line_no])
	naomi_blocks = [float(item) for item in indata[line_no+1].split()]
	ken_blocks = [float(item) for item in indata[line_no+2].split()]
	process(case_no, number, naomi_blocks, ken_blocks)
	line_no += 3
