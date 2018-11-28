

T = int(raw_input())

for i in range(T):
	test_input = raw_input().split()
	Smax = int(test_input[0])
	S = map(int, test_input[1])
	
	running_total = 0
	total_added = 0
	current_index = 0
	while current_index < Smax:
		if S[current_index] == 0 and running_total==current_index:
			total_added = total_added + 1
			running_total = running_total + 1

		running_total = running_total + S[current_index]
		current_index = current_index + 1


	print("Case #" + str(i+1) + ": " + str(total_added) )

