
import sys

if __name__ == '__main__':
	file_in = sys.argv[1]
	file_out = sys.argv[2]

	with open(file_in,'r') as f_in:
		with open(file_out,'w') as f_out:
			testcases = int(f_in.readline())

			for i in range(testcases):
				line = f_in.readline()[0:-1].split(' ')
				c = float(line[0])
				f = float(line[1])
				x = float(line[2])

				r = 2.0
				t = 0.0

				while True:
					ct = (c / r) + x / (r + f)
					cx = x / r

					if cx > ct:
						t += c / r
						r += f
					else:
						t += x / r
						message = 'Case #%d: %f\n' % (i + 1,t)
						f_out.write(message)
						break



