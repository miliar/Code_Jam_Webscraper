import sys

def decision(C, F, X, current_rate):

	t1 = (X-C) / current_rate
	t2 = X / (current_rate+F)

	if t1 <= t2:
		return False

	else:
		return True


def main():
	f = open(sys.argv[1])
	fa = open('result_gcj2014_qr2.txt', 'w')
	n = int(f.readline())

	for i in range(n):
		iarr = [ float(x) for x in f.readline().split() ]
		C = iarr[0]
		F = iarr[1]
		X = iarr[2]

		current_rate = 2.0
		t = 0.0
		# no need to buy a farm
		if X <= C:
			t += X / current_rate
		# probably necessary
		else:
			t += C / current_rate

			while decision(C, F, X, current_rate) == True:
				current_rate += F
				t += C / current_rate

			t += (X-C) / current_rate

		fa.write('Case #'+str(i+1)+': '+'%.7f'%t+'\n')

	f.close()
	fa.close()


if __name__ == '__main__':
	main()




