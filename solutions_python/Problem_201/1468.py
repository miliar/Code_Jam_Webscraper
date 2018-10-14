
def print_status(occ, Ls, Rs):
	length = len(occ)
	output_string = "Ls: |"
	for i in range(length):
		if occ[i]:
			output_string += "v|"
		else:
			output_string += "%s|" % (str(Ls[i]))
	output_string += "\nRs: |"
	for i in range(length):
		if occ[i]:
			output_string += "v|"
		else:
			output_string += "%s|" % (str(Rs[i]))
	print output_string

if __name__ == "__main__":
	case_count = int(raw_input())
	for case in range(case_count):
		N, K = map(lambda x: int(x), raw_input().strip().split())
		#
		#
		#
		occupied = [False for i in range(N)]
		Ls       = [i     for i in range(N)]
		Rs       = [N-i-1 for i in range(N)]
		#
		#
		#
		# strategy: maximal min(Ls, Rs)
		#        => maximal max(Ls, Rs)
		#        => left-most one
		# print_status(occupied, Ls, Rs)
		for person in range(K):
			# 1) calculate and choose the stall
			choose_this_stall = -1
			max_of_min = None
			max_of_max = None
			for stall in range(N):
				if occupied[stall] == False:
					minn = min(Ls[stall], Rs[stall])
					maxx = max(Ls[stall], Rs[stall])
					if max_of_min == None or minn > max_of_min:
						choose_this_stall = stall
						max_of_min = minn
						max_of_max = maxx
					elif minn == max_of_min:
						if maxx > max_of_max:
							choose_this_stall = stall
							max_of_min = minn
							max_of_max = maxx
			# 2) occupy (update the $occupied$)
			occupied[choose_this_stall] = True
			# 3) update the $Ls$ and $Rs$
			# 3-1) updating $Ls$
			tmp_index = choose_this_stall + 1
			while tmp_index < N and (not occupied[tmp_index]):
				Ls[tmp_index] = tmp_index - choose_this_stall - 1
				tmp_index += 1 # going right
			# 3-2) updating $Rs$
			tmp_index = choose_this_stall - 1
			while tmp_index >= 0 and (not occupied[tmp_index]):
				Rs[tmp_index] = choose_this_stall - tmp_index - 1
				tmp_index -= 1 # going left
			# print "\n\nchoosing this stall: %d" % (choose_this_stall)
			# print_status(occupied, Ls, Rs)
		#
		#
		#
		print "Case #%d: %d %d" % (case + 1, max_of_max, max_of_min)
