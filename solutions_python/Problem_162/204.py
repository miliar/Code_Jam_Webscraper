MAX_N = 1000000 + 7

answer = [99999999999] * MAX_N

def my_reverse(x):
	return int(str(x)[::-1])


#queue = [(1, 1)]
import Queue

my_queue = Queue.Queue()
my_queue.put((1,1))

while not my_queue.empty():# len(queue) >= 1:
	#print len(my_queue)
	#print my_queue.size()
	a, b = my_queue.get() #queue[0]
	#queue = queue[1:]

	if a < MAX_N and answer[a] > b:
		answer[a] = b


		my_queue.put((a+1, b+1)) #queue.append( (a+1, b+1) )

		a = my_reverse(a)
		if a < MAX_N:
			my_queue.put((a, b+1)) #queue.append( (a, b+1) )	

"""
def find_solution(x, count):
	if x < MAX_N and solution[x] == 0:
		solution[x] = count

		find_solution(x+1, count+1)
		find_solution(my_reverse(x), count+1)

find_solution(1, 1)
"""

T = int(raw_input())

for test in range(1, T+1):
	N = int(raw_input())
	print "Case #{}: {}".format(test, answer[N])
