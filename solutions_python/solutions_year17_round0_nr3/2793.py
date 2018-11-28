import heapq
if __name__ == "__main__":
	t = input()
	for round_count in range(1,t+1):
		nk = raw_input().split(' ')
		n = int(nk[0])
		k = int(nk[1])
		bathroom = []
		heapq.heappush(bathroom,-n)
		for user in range(1,k+1):
			space = heapq.heappop(bathroom)
			space = -space
			left = None
			right = None
			if space % 2 == 1:
				left = (space-1)/2
				right = (space-1)/2
			else:
				left = (space/2)-1
				right = space/2
			if left != 0:
				heapq.heappush(bathroom, -left)
			if right !=0:
				heapq.heappush(bathroom, -right)
			if user == k:
				output = "Case #"+ str(round_count) + ": " + str(max(left,right)) + " " + str(min(left,right)) 
				print(output)

