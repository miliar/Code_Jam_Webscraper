from math import *


def solver(N, K):
	data = (N,1,0,0)
	counter = 1;
	prevData = data
	prevCounter = counter
	diff = 1
	prevDiff = diff
	if K == 1:
		return split(N)
	if K == N:
		return (0,0)


	while counter < K:
		prevData = data
		prevCounter = counter
		data = helper(data)
		counter = counter + totalNum(data)
		prevDiff = diff
		diff =  K - counter
		# print(data)
		# print(diff)
	if diff <= 0:
		if prevDiff <= data[1]:
			return split(data[0])
		else:
			return split(data[2])
	else:
		print("HELLO") 
		



def totalNum(d):
	return d[1] + d[3]
#(larger, lar_num, smaller, sm_num)
def helper(N):
	larger = N[0]
	lar_num = N[1]
	smaller = N[2]
	sm_num = N[3]

	if larger == 1: # then smaller is 0
		return (0,0,0,0)
	
	retLarger = 0
	retNumLg = 0
	retSmaller = 0
	retNumSm = 0


	counter = 0
	if larger % 2 == 0: # if larger is even
		temp = split(larger)

		return (temp[0], lar_num, temp[1], lar_num + 2*sm_num)
	else:
		temp = split(larger)
		temp1 = split(smaller)
		return (temp[0],lar_num*2 + sm_num,temp1[1],sm_num)




def sum(n):
	return int(1 * (1 - pow(2,n))/(1 - 2))


def split(num):

	if num > 1:
		if num % 2 == 0:
			temp = int(num/2)
			# split(temp)
			# split(temp-1)
			return (temp, temp-1)
		else:
			temp = int((num-1)/2)
			# split(temp)
			# split(temp)
			return (temp, temp)
	elif num == 1 or num == 0:
		return (0,0)


# print(solver(4,2))
# print(solver(634,516))
# print(solver(999,509))
# # print(helper((125, 1, 124, 7)))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	data = input().split(" ")
	N = int(data[0])
	K = int(data[1])
	ans = solver(N, K)
	print("Case #{}: {} {}".format(i, ans[0], ans[1]))