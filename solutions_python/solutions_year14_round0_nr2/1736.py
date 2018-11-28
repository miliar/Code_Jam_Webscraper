from sys import stdin,stdout

for t in range(int(stdin.readline())):
	c,f,x=map(float,stdin.readline().split())
	m =0
	time_taken = (x/2)
	current_rate = 2
	s=0
	next_possible_time_taken = round((round((c/current_rate),7) + round((x/(current_rate+f)),7)),7)

	#print(next_possible_time_taken)

	while (next_possible_time_taken < time_taken):
		time_taken = next_possible_time_taken
		s += round((c/current_rate),7)

		current_rate = round(current_rate+f ,7)
		next_possible_time_taken = round(s +(round((c/current_rate),7) + round((x/(current_rate+f)),7)),7)
		#print(next_possible_time_taken)

	print('Case #'+str(t+1)+': '+ str(time_taken))

