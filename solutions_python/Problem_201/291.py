def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('C-large.in', 'r'), open('C-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	N, K = [int(x) for x in in_file.readline().split()]
	segments = {N : 1}
	counted = 0

	done = False
	while not done:
		for segment in sorted(segments.keys())[::-1]:
			count = segments[segment]
			del segments[segment]
			K = K - count
			counted += count
			if segment % 2 != 0:
				if segment // 2 != 0:
					if segment // 2 in segments:
						segments[segment // 2] += count * 2
					else:
						segments[segment // 2] = count * 2
			else:
				if segment // 2 != 0:
					if segment // 2in segments:
						segments[segment // 2] += count
					else:
						segments[segment // 2] = count
				if segment // 2 != 0:
					if segment // 2 - 1 in segments:
						segments[segment // 2 - 1] += count
					else:
						segments[segment // 2 - 1] = count
			if K <= 0:
				done = True
				if segment % 2 != 0:
					maximum = segment // 2
					minimum = segment // 2
				else:
					maximum = segment // 2
					minimum = segment // 2 - 1
				break
	epilogue(str(maximum) + " " + str(minimum), case_num)