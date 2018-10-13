
def main():
	num_tests = int(input())
	for case in range(num_tests):
		solve(case+1)

def solve(case):
	digits = list(input())

	fail_pos = None

	
	i = 1
	while i < len(digits):
		if digits[i-1] > digits[i]:
			i -= 1
			break

		i += 1


	if i == len(digits):
		print_solution(case, digits)
		return

	while i > 0 and digits[i-1] == digits[i]:
		i -= 1

	digits[i] = decrement(digits[i])

	ans = digits[:i+1] + list('9' * (len(digits) - (i+1)))
	print_solution(case, ans)


def decrement(x):
	return str(int(x) - 1)


def print_solution(case, ans):
	if ans[0] == '0':
		ans = ans[1:]

	ans = ''.join(ans)
	print('Case #{}: {}'.format(case, ans))

	
main()