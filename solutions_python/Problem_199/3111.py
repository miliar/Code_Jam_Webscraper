def num_flips(input_state, flipper_size):
	n = 0
	for i in range(len(input_state)):
		if not input_state[i]:
			if (i + flipper_size) > len(input_state):
				n = "IMPOSSIBLE"
				break
			else: # Flip!
				n += 1
				for j in range(flipper_size):
					input_state[i + j] = not input_state[i + j]
	return n
	
def convert_state(plus_minus):
	boolean_array = [False] * len(plus_minus)
	for i in range(len(plus_minus)):
		if (plus_minus[i] == '+'):
			boolean_array[i] = True
	return boolean_array
	
t = int(input())
for i in range(1, t + 1):
	s, k = input().split(" ")
	print("Case #{}: {}".format(i, num_flips(convert_state(s), int(k))))
	