def standing_ovation(audience):
	friends = 0
	current_clappers = 0
	for S,num_people in enumerate(audience):
		num_people  = int(num_people)
		if current_clappers < S:
			friends += (S-current_clappers)
			current_clappers = S
		current_clappers += num_people
	return friends

T = int(input())
for case in range(1,T+1):
	_ , audience = input().split()
	print('Case #{0}: {1}'.format(case, standing_ovation(audience)))

