def it_fits(x, y, R, C):
	if (x <= R and y <= C):
		return True
	elif (x <= C and y <= R):
		return True
	else:
		return False


if __name__ == '__main__':
	T = int(raw_input())

	for i in xrange(0, T):
		input_line = raw_input().split()
		X = int(input_line[0])
		R = int(input_line[1])
		C = int(input_line[2])

		if X >= 7:
			print "Case #%d: RICHARD" %(i+1)
		elif (R*C - X) % X != 0:
			print "Case #%d: RICHARD" %(i+1)
		elif (R == 2 or C == 2) and (X == 4 or X == 6):
			print "Case #%d: RICHARD" %(i+1)
		else:
			x_dimension = X
			y_dimension = 1
			winner = "GABRIEL"

			while(y_dimension < X):
				if (it_fits(x_dimension, y_dimension, R, C)):
					x_dimension -= 1
					if x_dimension*y_dimension < X:
						y_dimension += 1
				else:
					winner = "RICHARD"
					break

			print "Case #%d: %s" %(i+1, winner)


