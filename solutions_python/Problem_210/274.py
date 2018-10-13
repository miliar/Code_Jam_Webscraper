import sys


def solve(Ac,Aj):
	# start; end
	allA = []

	# start; end; index
	for a in Ac:
		allA.append((a[0],a[1],0))

	for a in Aj:
		allA.append((a[0],a[1],1))

	# compute slacks and inter
	allA.sort(key=lambda x:x[0])

	first = allA[0]
	last = allA[len(allA) - 1]

	# append the first at the end to close the loop
	allA.append((first[0] + 60*24,first[1] + 60*24,first[2]))

	# append the last at the beginning to start the loop
	allA = [(last[0] - 60*24,last[1] - 60*24,last[2])] + allA

	starting = True

	my = []
	
	prevTime = allA[0][1]

	curMy = {}
	for i in range(1,len(allA)-1):
		cur = allA[i]

		if starting:
			curMy['index'] = cur[2]
			curMy['duration'] = cur[1] - cur[0]
			curMy['slack'] = cur[0] - prevTime
			curMy['inter'] = []
			starting = False

		else:
			if cur[2] == curMy['index']:
				curMy['inter'].append((prevTime, cur[0]))
				curMy['duration'] = curMy['duration'] + (cur[1] - prevTime)
			else:
				curMy['slack'] = curMy['slack'] + (cur[0] - prevTime)
				my.append(curMy)
				curMy = {}
				curMy['index'] = cur[2]
				curMy['slack'] = cur[0] - prevTime
				curMy['duration'] = cur[1] - cur[0]
				curMy['inter'] = []

		prevTime = cur[1]

	curMy['slack'] = curMy['slack'] + (allA[len(allA)-1][0] - prevTime)
	my.append(curMy)

	# merge first and last if needed!
	if my[0]['index'] == my[len(my)-1]['index']:
		curMy = {}
		if len(my) - 1 != 0:
			
			curMy['index'] = my[0]['index']
			curMy['inter'] = my[0]['inter'] + my[len(my)-1]['inter'] + [(allA[0][1]+24*60, allA[1][0]+24*60)]
			curMy['slack'] = my[0]['slack'] + my[len(my)-1]['slack'] - 2*(allA[1][0] - allA[0][1])
			curMy['duration'] = my[0]['duration'] + my[len(my)-1]['duration'] + (allA[1][0] - allA[0][1])
			del my[len(my)-1]
			del my[0]

		else:
			curMy['index'] = my[0]['index']
			curMy['inter'] = my[0]['inter'] + [(allA[0][1]+24*60, allA[1][0]+24*60)]
			curMy['slack'] = my[0]['slack'] - 2*(allA[1][0] - allA[0][1])
			curMy['duration'] = my[0]['duration'] + (allA[1][0] - allA[0][1])
			del my[0]

		my.append(curMy)
	

	if len(my) == 1:
		minSW = 0
	else:
		minSW = len(my)

	# aggregate data
	agg = []
	for index in range(2):
		agg.append({'duration' : 0, 'inter' : [], 'slack' : 0})

	for el in my:
		agg[el['index']]['duration'] += el['duration']
		agg[el['index']]['inter'] += el['inter']
		agg[el['index']]['slack'] += el['slack']
	

	# find one with max duration
	if agg[0]['duration'] < agg[1]['duration']:
		agg.reverse()

	duration = agg[0]['duration']
	inter = agg[0]['inter']
	inter.sort(reverse=True)

	while(duration > 720):
		el = inter.pop()
		duration = duration - (el[1] - el[0])
		minSW = minSW + 2

	if(len(Ac) + len(Aj) > 2):
		raise Exception("not supported")

	if(len(Ac) == len(Aj)):
		#print("expected 2")
		return 2
	else:
		if(allA[2][1] - allA[1][0] > 720 and (allA[1][1] + 24*60) - allA[2][0] > 720):
			#if minSW != 4:
			#print("expected 4")
			return 4
				#raise Exception("bbb " + str(minSW))
		else:# minSW != 2:
			#print(len(allA))
			#print("expected 2")
			return 2
			#raise Exception("ccc")


	#return minSW


t = int(raw_input())
for i in range(1, t + 1):
	NAc,NAj = [int(s) for s in raw_input().split(" ")]
	# start; end
	Ac = []
	Aj = []
	for l in range(NAc):
		values = [int(s) for s in raw_input().split(" ")]
		Ac.append((int(values[0]), int(values[1])))

	for l in range(NAj):
		values = [int(s) for s in raw_input().split(" ")]
		Aj.append((int(values[0]), int(values[1])))

	result = solve(Ac,Aj)

	print("Case #{}: {}".format(i, result))
