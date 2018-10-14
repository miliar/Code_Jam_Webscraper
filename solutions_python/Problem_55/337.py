from sys import stdin

def get_int_arr():
	return [int(x) for x in stdin.readline().split(' ')]

def take_a_ride(groups, k):
	num = 0
	pos = 0
	for i in range(len(groups)):
		if num + groups[i] <= k:
			num += groups[i]
			pos = i
		else:
			break
	return (groups[pos+1:]+groups[:pos+1], num)

def solve():
	R, k, N = get_int_arr()
	queue = get_int_arr()

	total_earn= 0

	possibles = []
	p_earn = []

	while R > 0:
		newqueue, fare = take_a_ride(queue, k)
		if newqueue not in possibles:
			possibles.append(newqueue)
			p_earn.append(fare)
			queue = newqueue
			total_earn += fare
			R -= 1
		else:
			offset = possibles.index(newqueue)
			if offset -1 >= 0 and possibles[offset-1] == queue:
				period_earn = sum(p_earn[offset:])
				total_earn += int(R / (len(possibles)-offset)) * period_earn


				R %= (len(possibles)-offset)
				total_earn += sum(p_earn[offset:offset+R])
				break
			else:
				possibles.append(newqueue)
				p_earn.append(fare)
				queue = newqueue
				total_earn += fare
				R -= 1
	print total_earn

T = int(stdin.readline())
for case in range(T):
	print 'Case #%d:' % (case+1),
	solve()
