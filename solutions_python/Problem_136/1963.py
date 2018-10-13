'''
Problem B: Cookie Clicker Alpha
@author: peggyli
'''

if __name__ == '__main__':
	t = int(raw_input())

	for i in xrange(1, t+1):
		rate = 2 # 2 cookies/second

		# C = cost of cookie farm
		# F = extra F cookies/s from farm
		# X = cookies needed to win
		C, F, X = map(float, raw_input().split())

		# seconds to buy farm = C/rate
		# seconds to win = X/rate

		# should buy farm if time to buy farm + time to win with higher rate
		# < time to win at slower current rate

		time = 0.0

		while C/rate + X/(rate + F) < X/rate:
			time += C/rate
			rate += F

		time += X/rate
		print 'Case #%d: %.7f' % (i, time)