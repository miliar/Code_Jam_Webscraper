
from copy import deepcopy

def is_result(pancak_local, flip):

	# print pancak_local, flip

	global result

	# f = deepcopy(flip)

	if flip > result:
		return

	if not '-' in pancak_local:
		# print f, pancak_local
		if flip < result:
			result = flip
		return
	else:
		for i in xrange(0, len(pancak_local)-fliper_global+1):

			t_pan = ''
			for j in xrange(i, i+fliper_global):
				if pancak_local[j] == '+':
					t_pan += '-'
				else:
					t_pan += '+'

			pan = pancak_local[0:i] + t_pan + pancak_local[i+fliper_global:len(pancak_local)]

			# print f, pan
			# print len(check_list)

			if not pan in check_list:
				check_list[pan] = flip+1
				is_result(pan, flip+1)
			elif (flip+1) < check_list[pan] :
				check_list[pan] = flip+1
				is_result(pan, flip+1)


if __name__ == '__main__':

	t = int(raw_input()) 
	for i in xrange(1, t + 1):
		raw = raw_input()
		# print raw

		check_list = dict()
		result = 10000000000
		# fliper_global = 0

		pancakes, fliper = raw.split(' ')

		fliper_global = int(fliper)

		check_list[pancakes] = 0
		is_result(pancakes, 0)

		# print check_list

		if result == 10000000000:
			print 'Case #{}: {}'.format(i, 'IMPOSSIBLE')
		else:
			print 'Case #{}: {}'.format(i, result)

