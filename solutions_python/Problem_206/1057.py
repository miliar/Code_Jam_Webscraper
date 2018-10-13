# code jam round B - question 1

T = int(input().strip())
answers = []

for case in range(T):
	D, N = input().strip().split(' ')
	D, N = [int(D), int (N)]

	time_to_arrive = []

	for horse in range(N):
		K, S = input().strip().split(' ')
		K, S = [int(K), int(S)]

		time_to_arrive.append((D-K)/S)

	hours = max(time_to_arrive)

	answers.append(round((D / hours),6))

for index, answer in enumerate(answers):
	print('Case #' + str(index + 1) + ': ' + '%.6f' % answer)


