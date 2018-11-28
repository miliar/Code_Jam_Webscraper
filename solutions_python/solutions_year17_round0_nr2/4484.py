
def list_to_int(list):
	ret = 0
	for i in list:
		ret *= 10
		ret += i

	return ret

def solution(l, n):

	ans = [9] * l
	for j in range(9, 0, -1):
		for i in range(l):		
			ans[i] = j
			if list_to_int(ans) <= int(n):
				print("Case #{}:".format(tc + 1), list_to_int(ans))
				return 0

	return 1

def check(n):

	return n == "".join(sorted(n))

test_case = int(input())

for tc in range(test_case):

	n = input()

	l = len(n)

	p = 0
	ans = n

	for i in range(1, l):
		if n[i] < n[i-1]:
			ans = n[:p] + str(int(n[p]) - 1) + "9"*(l - p - 1)
		if n[i] > n[i-1]:
			p = i

	print("Case #{}:".format(tc + 1), int(ans))
				
