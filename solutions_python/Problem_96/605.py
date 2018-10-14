import sys
input = sys.stdin.readlines()

T = int(input[0][:len(input[0])-1])

for i in range(1, T+1):
	Tcase = input[i]
	if input[i][len(input[i])-1] == '\n':
		Tcase = input[i][:len(input[i])-1]
	Tcase = Tcase.split(' ')
	N = int(Tcase[0])
	S = int(Tcase[1])
	p = int(Tcase[2])
	ti = Tcase[3:]
	count = 0
	for tot in ti:
		if int(tot) >= p + (2*max(0,p-1)):
			count += 1
		elif int(tot) >= p + (2*max(0,p-2)):
			if S>0:
				count += 1
				S -= 1
	print 'Case #' + str(i) + ': ' + str(count)

