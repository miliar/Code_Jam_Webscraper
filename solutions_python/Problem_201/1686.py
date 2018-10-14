# @Author: Tushar Jain <tshrjn>
# @Date:   2017-04-09T06:52:28+05:30
# @Filename: bathroom.py
# @Last modified by:   tshrjn
# @Last modified time: 2017-04-09T07:08:53+05:30

from collections import defaultdict

def partition(n):
	if n%2 == 0:
		return n//2, n//2 - 1
	else:
		return (n-1)//2, (n-1)//2

def left_right_stalls(n,k ):
	left_right_dict = defaultdict(int)
	left_right_dict[n] = 1

	for i in range(k):
		choosen = max(left_right_dict.keys())
		left_right_dict[choosen] -= 1

		if left_right_dict[choosen] == 0:
			del left_right_dict[choosen]

		ls, rs = partition(choosen)
		left_right_dict[ls] += 1
		left_right_dict[rs] += 1
	return ls,rs

t = int(input())
for i in range(t):
    n,k = list(map(int,input().split()))

    ans = left_right_stalls(n,k)
    print("Case #{}: {} {}".format(i+1 , ans[0], ans[1]))
