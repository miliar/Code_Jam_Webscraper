tescases = int(raw_input())
for j in range(tescases):
	bestste = 0
	ferdig = True
	nonEmptyPlates = int(raw_input())
	pannekaker = [int(k) for k in raw_input().split(' ')]
	for i in pannekaker:
		if i> bestste:
			bestste = i
	antall = 0
	while ferdig:
		storste = 0
		plass = -1
		nums = 0
		for i in range(len(pannekaker)):
			if pannekaker[i]>storste:
				storste = pannekaker[i]
				plass = i
				nums = 0
			elif pannekaker[i] == storste:
				nums +=1
		bestste = min(bestste, storste + antall)
		if storste != 9 or nums >0 or 5 in pannekaker:
			if(storste>3):
				if(storste%2 == 0):
					pannekaker[plass] = storste/2
					pannekaker.append(storste/2)
				else:
					pannekaker[plass]= storste/2 +1
					pannekaker.append(storste/2)
				antall +=1
			else:
				ferdig = False
		else:
			pannekaker[plass]= 6
			pannekaker.append(3)
			antall +=1


	storste = 0
	for i in range(len(pannekaker)):
		if pannekaker[i]> storste:
			storste = pannekaker[i]
	bestste = min(bestste, storste + antall)
	print "Case #" + str(j+1) + ":", bestste