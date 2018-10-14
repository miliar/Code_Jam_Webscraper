
t = int(input())

for i in range(t):

	D, N = [int(i) for i in input().split()]

	min_time = -1
	for j in range(N):
		ki, si = [int(i) for i in input().split()]
		ti = (D-ki)/si # time of arrival in hours
		
		# print("for", j, ":", ti)

		if (min_time < 0 or ti > min_time):
			min_time = ti


	print("Case #" + str(i+1) + ": {0:.6f}".format( D/min_time))