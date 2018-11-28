import math 

T = int(input())

for j in range(T):
	N, K = map(int, input().split(" "))

	split_into = 2**int(math.log(K,2))
	occupied = split_into - 1
	remain_person = K-occupied
	remain_bathroom = N - occupied
	# print(split_into, occupied, remain_person)

	min_lr = remain_bathroom//split_into
	max_lr = min_lr+1
	# num of max = min_lr + 1
	num_max = remain_bathroom % split_into 
	num_min = split_into - num_max
	# print(min_lr, max_lr, num_min, num_max)

	if remain_person > num_max:
		# need to split min_lr
		max_lr = math.ceil((min_lr-1)/2)
		min_lr = (min_lr-1)//2
	else:
		# only split max
		min_lr = (max_lr-1)//2
		max_lr = math.ceil((max_lr-1)/2)

	print("Case #" + str(j+1) + ": " + str(max_lr) + " " + str(min_lr))

