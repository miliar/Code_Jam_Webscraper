fileIn = open('x2l.in', 'r')
fileOut = open('x2l.out', 'w')

T = int(fileIn.readline().strip())

for case in range(1, T+1):
	C, F, X = (float(x) for x in fileIn.readline().strip().split())

	cookies_second = 2.0
	total_time = 0.0

	while X / cookies_second > (X / (cookies_second + F)) + C / cookies_second:
		total_time +=  C / cookies_second

		cookies_second += F

	total_time += X / cookies_second
	fileOut.write("Case #{}: {}\n".format(case, total_time))