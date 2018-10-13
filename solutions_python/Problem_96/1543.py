def analyze_scores():
	
	with open('B-largein.txt', 'rb') as f:
		cases = int(f.readline())
		outstring = ''

		for idx in range(cases):
			case = f.readline().split(' ')

			# Parse case info out.
			dancers = int(case[0])
			surprising = int(case[1])
			max_score = int(case[2])
			scores = [int(i) for i in case[3:]]

			googlers = 0
			for score in scores:
				if score < max_score:
					continue
				if (3 * max_score - 2) <= score:
					googlers += 1
				elif (3 * max_score - 4) <= score and surprising > 0:
					googlers += 1
					surprising -= 1

			outstring += "Case #%i: " % (idx + 1)
			outstring += "%s\n" % str(googlers)

	with open('Boutput.txt', 'w') as f:
		f.write(outstring)
	print outstring
