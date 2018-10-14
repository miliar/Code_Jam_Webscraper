import sys

def main():
	in_file           = open(sys.argv[1], 'r')
        in_file_str       = in_file.read()
        in_file_list      = in_file_str.split('\n')

        out_file          = open('cookie_clicker_out.txt', 'w')

        num_test_cases    = int(in_file_list[0])
        case_counter      = 1
        in_file.close()
	
	for i in xrange(1, len(in_file_list) - 1):
		string  = in_file_list[i]
		list    = string.split()
		C       = float(list[0])
		F       = float(list[1])
		X       = float(list[2])
		
		cookie_rate            = 2.0000000	
		best_guess             = 0
		prev_best_guess        = X/cookie_rate
		seconds_to_cookie_farm = 0
		while 1:
			seconds_to_cookie_farm += C/cookie_rate
			cookie_rate            += F
			best_guess             	= seconds_to_cookie_farm + X/cookie_rate
			if (best_guess < prev_best_guess):
				prev_best_guess = best_guess
			else:
				total_seconds = prev_best_guess
				break

		out_file.write('Case #' + str(case_counter) + ': ' + str(total_seconds) + '\n')
		case_counter += 1
	out_file.close()

if __name__ == "__main__":
	main()
			
		

