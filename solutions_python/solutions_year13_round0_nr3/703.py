def is_pali(x):
	rev_x = 0
	tmp = x
	while tmp:
		rem = tmp % 10
		rev_x = rev_x * 10  + rem
		tmp = tmp / 10
	return x == rev_x


def all_pali_sqrs_up_to(up_to):
	num = 1
	skip = 3
	base = 1
	pali_sqrs = []
	while num < up_to:
            if is_pali(base):
                if is_pali(num):
        		pali_sqrs.append(num)
	    num += skip
            skip += 2
            base += 1
	return pali_sqrs

def num_of_pali_sqrs_in_range(pali_sqrs, start, end):
    return len([x for x in pali_sqrs if start <= x and x <= end])

def solve(input_filename, output_filename):
    pali_sqrs = all_pali_sqrs_up_to(10**14)
    
    output_lines = []
    input_lines = [x.strip() for x in open(input_filename).readlines()]
    num_cases = int(input_lines[0])
    
    for i in xrange(num_cases):
        start = int(input_lines[i+1].split()[0])
        end = int(input_lines[i+1].split()[1])
        sol = num_of_pali_sqrs_in_range(pali_sqrs, start, end)
        output_lines.append("Case #%s: %s\n" % (i+1, sol))

    open(output_filename, "w").writelines(output_lines)
