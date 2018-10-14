import time

with open('o2', 'w+') as output:
	with open('t2', 'r+') as fle:
		cases = int(fle.readline())
		curCase = 0
		for i in range(cases):
			curCase += 1
			print("Case " +str(curCase))
			r = 2.0
			v = fle.readline().split()
			c = float(v[0])
			f = float(v[1])
			x = float(v[2])
			t = 0.0
			mC = 0
			print(c)
			print(f)
			print(x)
			while True:
				if x / r > (x / (r + f) + (c / r)):
					t += (c / r)
					r += f
				else:
					t += (x / r)
					break
			print(t)
			output.write('Case #' + str(curCase) + ': ' + str(t) + '\n')

