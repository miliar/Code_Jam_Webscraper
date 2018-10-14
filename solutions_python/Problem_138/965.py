if __name__ == "__main__":
	with open("D-large.in", 'r') as inputf:
		outputf=open("D_large_out.out",'w')
		line = inputf.readline()
		line = line.rstrip('\n')
		test_num = int(line)

		for test in range(test_num):
			line = inputf.readline()
			line = line.rstrip('\n')
			num = int(line)

			line = inputf.readline()
			line = line.rstrip('\n')
			naomi_1 = line.split(' ')
			naomi_1.sort()
			naomi_2 = naomi_1[:]

			line = inputf.readline()
			line = line.rstrip('\n')
			ken_1 = line.split(' ')
			ken_1.sort()
			ken_2 = ken_1[:]

			dec_win = 0
			war_win = 0

			for i in range(num):
				if naomi_1[0] < ken_1[0]:
					naomi_1.pop(0)
					ken_1.pop()
				else:
					naomi_1.pop(0)
					ken_1.pop(0)
					dec_win = dec_win+1

			for i in range(num):
				ken_win = False
				for j in range(num-i):
					if naomi_2[0] < ken_2[j]:
						naomi_2.pop(0)
						ken_2.pop(j)
						ken_win = True
						break
				if ken_win == False:
					war_win = num - i
					break
			result = "Case #%d: %d %d" % (test+1, dec_win, war_win)
			outputf.write(result)

			if test!=test_num-1:
				outputf.write('\n')
		