def main():
	cases = int(input())
	for i in range(cases):
		line = input()
		line = line.split()
		c = float(line[0])
		f = float(line[1])
		x = float(line[2])
		time_total = 0.0
		f_num = 0
		end = 0.0
		while(True):
			current_total = time_total + time_to_go(x, f, f_num)
			buy_future = time_total + time_to_go(c, f, f_num) + time_to_go(x, f, f_num+1)

			if current_total < buy_future:
				end = current_total
				break

			else:
				time_total += time_to_go(c, f, f_num)
				f_num += 1
		print("Case #%d: %f" % (i+1, end))


def time_to_go(x, f, f_num):
	return x/(2+f*f_num)
main()