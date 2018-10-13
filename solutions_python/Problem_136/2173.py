import sys

def oneRun(x, k, f):
	c_speed = 2.0
	tot_t = 0.0
	while(1):
		t1 = x/c_speed
		t2 = x/(c_speed + f) + k/(c_speed)

		if (t1 < t2):
			return (tot_t + t1)
		else:
			tot_t +=(k/c_speed) 
			c_speed += f








if __name__ == '__main__':
	in_f = open(sys.argv[1])

	num = int(in_f.readline())
	mnum = num

	while(num):
		l = in_f.readline()
		la = [float(i) for i in l.split(' ')]
		k, f, x = la[0], la[1], la[2]
		print("Case #%d: %.7f"%(mnum - num + 1, oneRun(x, k, f)))
		num -= 1
