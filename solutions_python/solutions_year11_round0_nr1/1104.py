import codejamhelper as h

cases = h.get_case_list(h.get_file())

solutions = []

for case in cases:
	jobList = []
	items = case.split()
	for item in xrange(1,len(items),2):
		jobList.append([items[item],int(items[item+1])])
	positionOrange = 1
	positionBlue = 1
	time = 0
	jobPos = 0
	while True:
		nextJob = False
		if jobList[jobPos][0] == "O":
			if jobList[jobPos][1] != positionOrange:
				if positionOrange > jobList[jobPos][1]:
					positionOrange -= 1
				else:
					positionOrange += 1
			else:
				nextJob = True
			nextOtherJob = jobPos+1
			while nextOtherJob < len(jobList):
				if jobList[nextOtherJob][0] == "B":
					if jobList[nextOtherJob][1] != positionBlue:
						if positionBlue > jobList[nextOtherJob][1]:
							positionBlue -= 1
						else:
							positionBlue += 1
					break
				nextOtherJob += 1
		if jobList[jobPos][0] == "B":
			if jobList[jobPos][1] != positionBlue:
				if positionBlue > jobList[jobPos][1]:
					positionBlue -= 1
				else:
					positionBlue += 1
			else:
				nextJob = True
			nextOtherJob = jobPos+1
			while nextOtherJob < len(jobList):
				if jobList[nextOtherJob][0] == "O":
					if jobList[nextOtherJob][1] != positionOrange:
						if positionOrange > jobList[nextOtherJob][1]:
							positionOrange -= 1
						else:
							positionOrange += 1
					break
				nextOtherJob += 1
		if nextJob == True:
			jobPos += 1
		time += 1
		if jobPos == len(jobList):
			break
	solutions.append(time)

h.put_file(solutions)
