T = int(input())
case = 1
while T>0:
	T -= 1
	[D, N] = [int(x) for x in raw_input().strip().split(' ')]
	Horses = []
	for i in range(N):
		[Ki, Si] = [int(x) for x in raw_input().strip().split(' ')]
		Horses.append((Ki, Si))

	speed = None
	for (k, v) in Horses:
		dst = float(D - k)
		t = dst/float(v)
		#print(t)
		myv = float(D) / t
		if speed == None:
			speed = myv
		else:
		 	speed = min(speed, myv)
	print('Case #' + str(case) + ': ' + str(speed))
	#print(Horses)
	case += 1


