import sys

def solve(d, n, horse):
	horse.sort()
	t = [None]*n
	for i in range( 0, n ):
		t[i] = ( d - horse[i][0] ) / horse[i][1]

	max_t = max(t)
	print(d/max_t)

T = int(input())
for i in range(0, T):
	[d, n] = [int(a_temp) for a_temp in input().strip().split(' ')]
	horse = [None]*n
	for j in range(0, n):
		horse[j] = [int(a_temp) for a_temp in input().strip().split(' ')]
	print("Case #",i+1,": ",sep="",end="")
	solve(d, n, horse)
