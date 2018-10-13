"""Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ N ≤ 1000.
Large dataset

1 ≤ N ≤ 1018.
Sample


Input 
 	
Output 
 
4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

Note that the last sample case would not appear in the Small dataset.
"""

def tidy(N):
	""" returns the biggest tidy number <= N """
	N = str(N)

	ans = 0
	prev = 0

	equal_cnt = 1

	ALL_NINES = False

	for i in N:
		i = int(i)
		if ALL_NINES:
			ans = ans*10 + 9

		elif i < prev:
			if equal_cnt == 1:
				ans -= 1
				ans = ans*10 + 9
			else:
				
				ans = str(ans)[:-equal_cnt]
				ans += str(prev-1) + '9'*(equal_cnt)
				ans = int(ans)

			ALL_NINES = True
		else: # i >= prev
			if i == prev:
				equal_cnt += 1
			else:
				equal_cnt = 1
			ans = ans*10 + i
			prev = i

	return ans


t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
  N = int(input())

  print("Case #{}: {}".format(i, tidy(N)))
