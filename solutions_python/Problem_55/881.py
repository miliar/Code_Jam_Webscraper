#!/usr/bin/env python

"""
	1. some go alone
	2. some go in groups - and only want to go together

	$1 a ride
	every one who goes on it will want to go again.

	k people.
	people queue for it in groups - board once ata time until there are no more groups / room for the next group.

	it still goes if it is full or not.

	re-queue in the same order - > RUNS R times a day.

	R=4 k=6	4 groups -
	1, 4 ,2 ,1
		-> [1,4] # 5
	2 1 1 4
		-> [2 1 1 ] # 4
	4 2 1 1
		-> [4, 2 ] # 6
	1 1 4 2
		->  1 1 4  # 6

	= 21 $

------------

input:
1|T -> number of test cases
2| R k N
3| N groups  g0 = group 1 size - g1 group 2 size.
----
output:
Case #x: y"
x = case number
y = euros made


limits -> 1 <= T <= 50
gi <= k

smallest:
1 <= R <= 1000   # max 1000 runs min 1 run
1 <= k <= 100 # min hold at once1 =  and max is 1000
1 <= N <= 10 - > number of groups
1 <= group size <= 10

"""
from collections import deque

def compute_stuff(R, k, N, groups):
	total = 0
	for i in range(0, R):
		sum = 0
		counter = 0
		while(sum <=k and counter < N):
			if (sum + groups[0] <= k):
				sum += groups[0]
				groups.append(groups[0])
				groups.popleft()
			counter = counter +1
		total += sum
	return total


f = open ("example.txt")
data = f.readlines()
test_num =  int(data[0])
counter = 1

datazzz = []

for i in range(1, test_num*2+1):
	if i %2 == 0:
		pass
	else:
		temp_t = (data[i], data[i+1])
		datazzz.append(temp_t)

for rkn, group_d in datazzz:
	result = []
	R = int(rkn.split()[0])
	k = int(rkn.split()[1])
	N = int(rkn.split()[2])
	temp = []
	for x in group_d.split():
		temp.append(int(x))
	groups =  deque(temp)
	print "Case #" +str(counter) + ": " + str( compute_stuff(R, k, N, groups) )
	counter = counter +1






