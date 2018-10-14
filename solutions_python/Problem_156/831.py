import math

T = int(input())

for x in range(1, T+1):
	D = int(input())
	diners = sorted(list(map(int, input().split())), reverse=True)

	MIN_MINUTES = max(diners)
	current_splits = 0
	min_minutes = max(diners)
	# If current_splits ever exceeds MIN_MINUTES return min_minutes

	split_9_once = True
	if diners.count(9) == 1:
		split_9_once = False

	while current_splits < MIN_MINUTES:
		# IF OUR MAX STACK IS 3 ITS ALWAYS MORE EFFICIENT
		# TO LET THE CUSTOMERS ENJOY AND EAT
		if diners[0] <= 3:
			break
		to_split = diners.pop(0)

		# IF THERE IS ONLY ONE NINE WE ONLY SPLIT TWICE
		# OTHERWISE WE ONLY SPLIT ONCE
		if not split_9_once and to_split == 9:
			if len(diners) > 0:
				if diners[0] <= 4 or diners[0] == 6:
					split = 3
				else:
					split = math.ceil(to_split / 2)
			else:
				split = 3
		else:
			split = math.ceil(to_split / 2)

		# APPEND SPLIT VALUES TO DINERS LIST
		diners.append(to_split - split)
		diners.append(split)
		diners = sorted(diners, reverse=True)

		# INCREASE SPLITS BY ONE
		current_splits += 1
		min_minutes = min(min_minutes, current_splits + max(diners))


	# print(diners)
	print('Case #{0}: {1}'.format(x, min_minutes))


'''
MAX_DINERS = 6
MAX_PANCACKES = 9
  Splits + Max = Minutes To Eat
9 ->  2    3  =  5
      1    5  =  6
8 ->  1    4  =  5
7 ->  1    4  =  5
6 ->  1    3  =  4
5 ->  1    3  =  4
4 ->  1    2  =  3
3 ->  0    3  =  3
2 ->  0    2  =  2
1 ->  0    1  =  1
'''