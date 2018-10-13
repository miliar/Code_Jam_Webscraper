import bisect

def return_tuple(N):
	if N % 2 == 0:
		return (int(N/2), int(N/2-1)) # R then L
	else:
		return (int((N-1)/2), int((N-1)/2))


def solution(N,K):
	places_left = [N]

	for _ in range(K):
		current = places_left.pop()
		L = return_tuple(current)[1]
		R = return_tuple(current)[0]

		position = bisect.bisect(places_left, L)
		bisect.insort(places_left, L)
		position = bisect.bisect(places_left, R)
		bisect.insort(places_left, R)
		
	x = return_tuple(current)

	return str(max(x)) + ' ' + str(min(x))
	

# start

T = int(input().strip())

for _ in range(T):
	N, K = input().strip().split(' ')
	N, K = [int(N), int(K)]



	print('Case #' + str(_+1) + ':', solution(N, K))
