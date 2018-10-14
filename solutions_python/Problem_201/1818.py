
import math

result = [None, None]

def cal(n, k):

	global result

	# if k > (math.ceil(float(n)/2)+5):
	# 	result = [0, 0]
	# 	# print 'reture by checking'
	# 	return

	# free_space_list = [n]

	# for i in xrange(k):

	# 	# free_space_list.sort(reverse=True)

	# 	if i == (k-1):
	# 		space = float(free_space_list[0]) - 1
	# 		result = [ int(math.ceil(space/2)), int(math.floor(space/2)) ]
	# 	else:
	# 		space = float(free_space_list.pop(0)) - 1
	# 		free_space_list.append(int(math.ceil(space/2)))
	# 		free_space_list.append(int(math.floor(space/2)))

	people = k

	free_space_list = [n]

	avail_list = dict()
	avail_list[n] = 1

	while not people < 0:

		# print free_space_list
		# print avail_list

		space = free_space_list.pop(0) 
		avail = avail_list[space]
		avail_list[space] = 0

		space = float(space - 1)

		if (people-avail) <= 0:
			result = [ int(math.ceil(space/2)), int(math.floor(space/2)) ]
			return

		people = people-avail

		ceil = int(math.ceil(space/2))
		floor = int(math.floor(space/2))

		if not ceil in free_space_list:
			free_space_list.append(ceil)
		if not ceil in avail_list:
			avail_list[ceil] = avail
		else:
			avail_list[ceil] += avail

		if not floor in free_space_list:
			free_space_list.append(floor)
		if not floor in avail_list:
			avail_list[floor] = avail
		else:
			avail_list[floor] += avail

		pass


if __name__ == '__main__':

	t = int(raw_input()) 
	for case in xrange(1, t + 1):
		raw = raw_input()
		# print raw

		n, k = raw.split(' ')
		n = int(n)
		k = int(k)

		cal(n, k)

		print 'Case #{}: {} {}'.format(case, result[0], result[1])


