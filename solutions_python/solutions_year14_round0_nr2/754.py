#!/usr/bin/env pythom
#coding: utf-8

def strategy(amount, rate, c, fr, x):
	time1 = float(x-amount) / rate
	time2 = float(x-amount+c) / (rate+fr)
	if time2 < time1:
		return True
	else:
		return False

if __name__ == '__main__':
	fname = 'B-large'
	with open('%s.in' % fname) as f, open('%s.out' % fname, 'w') as f2:
		n = int(f.readline())
		for i in xrange(n):
			c, fr, x = [float(x) for x in f.readline().strip().split()]
			rate = 2.0
			amount = 0.0
			time = 0.0
			while True:
				complete_time = (x-amount)/rate
				build_time = c/rate
				if complete_time < build_time:
					time += complete_time
					break
				else:
					time += build_time
					amount += c 
					judge = strategy(amount, rate, c, fr, x)
					if judge:
						amount -= c
						rate += fr
					else:
						time += (x-amount) / rate
						break
			f2.write('Case #%s: %.7f\n' % (i+1, time))
