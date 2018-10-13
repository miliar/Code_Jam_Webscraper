# Oversized pancake.

def oversizePancake(tc):
	
	case_num = 0
	
	while (tc != 0):

		pancake_string, K = raw_input().split()

		#print pancake_string, K

		count = 0

		for x in xrange(len(pancake_string) - int(K) + 1):

			if pancake_string[x] == '-':

				count += 1

				for i in xrange(x, x+int(K)):
					if pancake_string[i] == '-':
						pancake_string = list(pancake_string)
						pancake_string[i] = '+'
						''.join(pancake_string)
						#print pancake_string
					else:
						pancake_string = list(pancake_string)
						pancake_string[i] = '-'
						''.join(pancake_string)


		if '-' in pancake_string:
			answer = "IMPOSSIBLE"
		else:
			answer = count

		print "Case #{}: {}".format(case_num+1, answer)


		tc += 1
		case_num +=1

oversizePancake(input())

