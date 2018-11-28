# This is a standard python library
import heapq

def parseString(raw, w):
	count = 0
	for elem in raw:
		if count != 0:
			w.write('Case #' + str(count) + ': ')
			temp = list(map(int, elem.split()))
			w.write(' '.join(map(str, findSeats(temp))) + '\n')
		count += 1


def findSeats(temp):
	seats = temp[0]
	people = temp[1]
	if seats == people:
		return [0] * 2
	else:
		seatsInBetween = [int(seats * -1)]
		right = 0
		left = 0
		heapq.heapify(seatsInBetween)
		for i in range(0, people):
			maxDist = heapq.heappop(seatsInBetween) * -1
			right = maxDist // 2
			left = maxDist - 1 - right
			heapq.heappush(seatsInBetween, right * -1)
			heapq.heappush(seatsInBetween, left * -1)
		maxi = max(right, left)
		mini = min(right, left)
		return [maxi, mini]


f = open('C-small-2-attempt0.in', 'r')
w = open('output.txt', 'w')
raw = f.readlines()
parseString(raw, w)
