def is_tidy(x):

	
	x = [int(i) for i in str(x)]
	for index in range(0, len(x)-1):
		if x[index] <= x[index +1]:
			continue
		else:
			return 0
	return 1

def solution(N):
	while not is_tidy(N):
		x = [int(i) for i in str(N)]
		places = len(x) - 1 # 10 ^ (place -1 )

		for index in range(0, len(x)-1):
			
			if x[index] > x[index +1]:
				# first conflict
				break
			places -= 1
			
		N = (N - (10 ** places)) // (10 ** places) * (10 ** places) + (10 ** places - 1)
		# print("shift", N)
	return N
	

# start

T = int(input().strip())

for _ in range(T):
	N = int(input().strip())


	print('Case #' + str(_+1) + ':', solution(N))
