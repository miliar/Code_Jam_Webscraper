
def solve(N):
	nums = list(N)
	nums = [int(i) for i in nums]

	for i in range(len(nums) - 1, 0, -1):
		#print i
		if nums[i-1] > nums[i]:
			nums[i-1] -= 1
			for j in range(i, len(nums)):
				nums[j] = 9

	nums = [str(i) for i in nums]
	result = "".join(nums)
	result = result.lstrip("0")
	return result


def process_file(fname):
	f = open(fname, 'r')
	fo = open(fname + ".result", "w")

	lines = f.readlines()
	lines = [i.strip() for i in lines]

	num_samples = int(lines[0])
	lines = lines[1:]

	print("there are: %i samples" % num_samples)
	print("")

	case_num = 1
	for l in lines:
		result = solve(l)
		to_print = "Case #%i: %s\n" % (case_num, result)
		fo.write(to_print)
		case_num += 1

#print solve("110")
#process_file('sample.txt')
#process_file('B-small-attempt0.in')
process_file('B-large.in')