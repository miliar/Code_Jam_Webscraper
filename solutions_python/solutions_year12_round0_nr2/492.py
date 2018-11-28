def int_input():
	return int(raw_input())

def list_int_input():
	return [int(i) for i in raw_input().split()]

def is_best_result_without_surprise():
	return 

def solve():
	numbers = list_int_input()

	max_surprise = numbers[1]
	max_score = numbers[2]
	scores = numbers[3:]

	answer = 0

	for score in scores:
		if score < max_score:
			continue
		if score >= max(max_score*3-2, 0):
			answer += 1
		elif score >= max(max_score*3-4, 0) and max_surprise > 0:
			answer += 1
			max_surprise -= 1
	
	return answer

def main():
	for i in range(1, int_input()+1):
		print 'Case #%d: %s' % (i, solve())

main();