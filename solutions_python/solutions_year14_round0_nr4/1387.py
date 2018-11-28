for cases in range(1,int(raw_input()) + 1):
	num_rocks = int(raw_input())
	naomi_rocks  = map(float,raw_input().split())
	ken_rocks = map(float,raw_input().split())

	naomi_rocks.sort()
	ken_rocks.sort()

	temp_naimo = naomi_rocks[:]
	temp_ken = ken_rocks[:]
	
	normal_wins = 0
	cheating_wins = 0
	for rock_index in range(0,num_rocks):
		if naomi_rocks[0] < ken_rocks[0]:
			naomi_rocks.remove(naomi_rocks[0])
			ken_rocks.remove(ken_rocks[-1])
		else:
			naomi_rocks.remove(naomi_rocks[0])
			ken_rocks.remove(ken_rocks[0])
			cheating_wins += 1
	naomi_rocks = temp_naimo
	ken_rocks = temp_ken
	for naiomi_rock in reversed(naomi_rocks):
		if naiomi_rock > ken_rocks[-1]:
			ken_rocks.remove(ken_rocks[0])
			normal_wins += 1
		else:
			for ken_rock in ken_rocks:
				if ken_rock > naiomi_rock:
					ken_rocks.remove(ken_rock)
					break
	print 'Case #%d: %d %d' % (cases,cheating_wins,normal_wins)
