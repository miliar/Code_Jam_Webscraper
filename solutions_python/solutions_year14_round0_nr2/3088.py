#!/bin/env python3


def cookie_price(farms, C, F, X):
	total = X / (2.0 + farms * F)
	part = 0
	if farms >= 1:
		for i in range(farms):
			part += C / (2.0 + i * F)
	
	return total + part


def test():
	time = cookie_price(3, 500.0, 4.0, 2000.0)
	print("time: {}".format(time))

def calc_optimal(C, F, X):
	part = 0
	farm = 0
	running = True
	timeprev = float("inf")
	while running:
		t_1 = X / (2.0 + farm * F)
#		print("Price for farm {}:{}".format(farm, t_1 + part))
#		print("Compare with manual: {}".format(cookie_price(farm, C, F, X)))
		if timeprev < part + t_1:
			running = 0
		else:
			timeprev = part + t_1
			part += C / (2.0 + farm * F)
		farm = farm + 1

	return timeprev
	

def test_opt():
	time = calc_optimal(500.0, 4.0, 2000.0)
	print("time: {}".format(time))



test_opt()

def main():
	f_in = open("input.txt", "rt")
	f_out = open("output.txt", "wt")
	n = int(f_in.readline())
	for i in range(n):
		l = list(map(lambda x:float(x), f_in.readline().split()))
		o = calc_optimal(l[0], l[1], l[2])
		f_out.write("Case #{}: {}\n".format(i+1, o))
main()
