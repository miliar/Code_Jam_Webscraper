# Andre Guedes (Brazil)
#
# Google Code Jam 2010.
#

next = 0

input = []

def parse_input():
	global input
	file = open('input.txt', 'r')
	lines = file.readlines()[1:]
	idx = 0
	while idx < len(lines):
		l = lines[idx].strip().split(' ')
		idx += 1
		r = int(l[0])
		k = int(l[1])
		n = int(l[2])
		l = lines[idx].strip().split(' ')
		idx += 1
		queue = []
		for i in range(n):
			queue.append(int(l[i]))
		
		input.append((r, k, queue))

def fill_car(queue, k):
	global next
	sum = 0
	first = next
	while True:
		sum += queue[next]
		next += 1
		if next >= len(queue):
			next = 0
		
		if (sum + queue[next]) > k or first == next:
			break;
	return sum

def do_case(idx):
	global next
	money = 0
	next = 0
	r = input[idx][0]
	k = input[idx][1]
	queue = input[idx][2]

	for i in range(r):
		money += fill_car(queue, k)

	print 'Case #%d: %d' % (idx+1, money)

def main():
	global input
	parse_input()
	for i in range(len(input)):
		do_case(i)

if __name__ == '__main__':
	main()
