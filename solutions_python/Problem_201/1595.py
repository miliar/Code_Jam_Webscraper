f = open("bathroomStallsLarge.in", "r")
new_file = open("bathroomStallsLargeSol", "w")
t = int(f.readline())

def bathroom_stalls(n, k ):

	last_layer = find_last_layer(k)
	stalls_used = 2 ** (last_layer) - 1
	amount_in_layer = 2 ** (last_layer)
	# print amount_in_layer
	to_fill = k - stalls_used
	# print to_fill
	stalls_left = n - stalls_used
	# print stalls_left
	lower_number_in_layer = stalls_left/amount_in_layer
	# print lower_number_in_layer
	higher_number_in_layer = lower_number_in_layer + 1
	amount_higher = stalls_left -  stalls_left/amount_in_layer * amount_in_layer
	amount_lower = amount_in_layer - amount_higher

	if to_fill > amount_higher:
		left, right = left_right(lower_number_in_layer)
	else:
		left, right = left_right(higher_number_in_layer)
	return str(max(left,right)) + " " + str(min(left,right))

def find_last_layer(k):
	layer = 1
	while (2**layer - 1) < k:
		layer += 1
	return layer - 1

def left_right(n):
	if n % 2 == 1:
		return ((n-1)/2,(n-1)/2)
	else:
		return ((n)/2 - 1,(n)/2)

for i in range(1,t+1):
	n, k = [int(x) for x in f.readline().split(' ')]
	new_file.write("Case #"+str(i)+ ": "+str(bathroom_stalls(n,k))+"\n")