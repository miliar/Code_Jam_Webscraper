import sys
from bisect import bisect

def war(n_list,k_list):
	# n_list = list(n_list)
	k_list = list(k_list)

	n_score = 0

	for b in n_list:
		i = bisect(k_list,b)
		if i == len(k_list):
			k_list.pop(0)
			n_score += 1
		else:
			k_list.pop(i)

	return n_score


def dwar(n_list,k_list):
	# n_list = list(n_list)
	k_list = list(k_list)

	n_score = 0

	for b in n_list:
		i = bisect(k_list,b)

		if i == 0: # cannot beat any of his bricks
			k_list.pop() # concede by telling him you have (k[-1] + (k[-2] or 0)) / 2
		else:
			k_list.pop(i - 1) # tell him yours is (k[i - 1] + (k[i - 2] or 0.0)) / 2
			n_score += 1

	return n_score



if __name__ == '__main__':
	with open(sys.argv[1],'r') as f_in:
		with open(sys.argv[2],'w') as f_out:
			testcases = int(f_in.readline())

			for i in range(testcases):
				n = int(f_in.readline())
				n_list = map(lambda x: float(x),f_in.readline().split(' '))
				n_list.sort()
				k_list = map(lambda x: float(x),f_in.readline().split(' '))
				k_list.sort()

				war_score = war(n_list,k_list)
				dwar_score = dwar(n_list,k_list)

				f_out.write('Case #%d: %d %d\n' % (i + 1,dwar_score,war_score))


