#!/usr/bin/env python

def solve():
	C , J = [int(i) for i in raw_input().split()]
	ActivitiesC = [[int(i) for i in raw_input().split()] for _ in xrange(C)]
	ActivitiesJ = [[int(i) for i in raw_input().split()] for _ in xrange(J)]
	if (C <= 1 and J <= 1):
		return 2
	ActivitiesC.sort()
	ActivitiesJ.sort()
	if (C == 0):
		if (ActivitiesJ[1][1] - ActivitiesJ[0][0] <= 720 or 24*60 - ActivitiesJ[1][0] + ActivitiesJ[0][1] <=720):
			return 2
		else:
			return 4
	if (J == 0):
		if (ActivitiesC[1][1] - ActivitiesC[0][0] <= 720 or 24*60 - ActivitiesC[1][0] + ActivitiesC[0][1] <=720):
			return 2
		else:
			return 4
	flag = 0
	for x ,y in ActivitiesJ:
		if (x > ActivitiesC[0][1] and x < ActivitiesC[1][0]):
			flag = 1
	if (flag == 0):
		# ta + anamesa
		if (ActivitiesC[1][1] - ActivitiesC[0][0] <= 720 and ActivitiesJ[1][0] - ActivitiesJ[0][1] >=720 or 24*60 - ActivitiesJ[1][0] + ActivitiesJ[0][1] <=720 and ActivitiesC[0][0] - ActivitiesJ[0][1] + ActivitiesJ[1][0] - ActivitiesC[1][1] >=720):
			return 2
		else:
			return 4
	flag = 0
	for x ,y in ActivitiesC:
		if (x > ActivitiesJ[0][1] and x < ActivitiesJ[1][0]):
			flag = 1
	if (flag == 0):
		#ta | anamesa
		if (ActivitiesJ[1][1] - ActivitiesJ[0][0] <= 720 and ActivitiesC[1][0] - ActivitiesC[0][1] >=720 or 24*60 - ActivitiesC[1][0] + ActivitiesC[0][1] <=720 and ActivitiesJ[0][0] - ActivitiesC[0][1] + ActivitiesC[1][0] - ActivitiesJ[1][1] >=720):
			return 2
		else:
			return 4
	return 4


def main():
    T = int(raw_input())
    for t in xrange(T):
    	sol = solve()
    	print "Case #{}: {}".format(t+1,sol)

if __name__ == '__main__':
	main()