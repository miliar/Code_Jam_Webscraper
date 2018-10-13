def case (case_num):
	C, F, X = [ float(i) for i in raw_input().split() ]
	C *= 1000000
	F *= 1000000
	X *= 1000000
	_F = 2.0 * 1000000

	cur_time = 0.0
	
	prev_time = X / _F
	
	_F += F

	second = 0.0

	while True:
		cur_time = X / _F
		tmpF = _F - F

		second += C / tmpF
		cur_time += second

		
		if cur_time > prev_time:
			print( "Case #{}: {:.7f}".format( case_num, prev_time ) )
			return

		_F += F
		prev_time = cur_time


if __name__ == "__main__":
	num_cases = int( raw_input() )
	for i in xrange( 1, num_cases + 1 ):
		case(i)
