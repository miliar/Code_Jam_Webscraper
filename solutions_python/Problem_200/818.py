import sys

def ayy_lmao(N_str):
	result = N_str[0]
	j = 0
	N_digits = len(N_str)
	while j < N_digits - 1 and N_str[j + 1] >= N_str[j]:
		result += N_str[j + 1]
		j += 1
	#we've done the initial part
	if(j == N_digits - 1):
		return result

	if result[-1] > '1':
		result = "" + ayy_lmao(str(int(result) - 1)) + ('9' * (N_digits - j - 1))
		result = result.lstrip('0')
		return result
	else:
		result = '9' * (N_digits - 1)
		return result

	



T = int(raw_input())

for i in xrange(1, T + 1):
	N_str = raw_input()
	print "Case #" + str(i) + ": " + ayy_lmao(N_str)

sys.stdout.flush()