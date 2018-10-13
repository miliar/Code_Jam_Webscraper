T = int(input())

for t in range(T):
	DN = input().split(' ')
	D, N = int(DN[0]), int(DN[1])
	horses = []
	max_time = 0
	
	for n in range(N):
		horse_string = input().split(' ')
		horse = (int(horse_string[0]),int(horse_string[1]))
		horses.append(horse)
	for horse in horses:
		time = (D-horse[0])/horse[1]
		if time>max_time:
			max_time = time
	
	speed = D/max_time
	print('Case #{}: {}'.format(t+1,speed))