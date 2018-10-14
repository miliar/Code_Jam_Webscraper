
def next_full(lis, i):
	if i >= len(lis):
		return i

	idx = i + 1
	while idx < len(lis):
		if lis[idx] == 1:
			return idx
		idx += 1
	return idx


def find_max_min(lis, i):
	a = 0
	b = 0
	idx = i + 1
	if idx >= len(lis):
		a = 0
	else:
		while lis[idx] != 1:
			a += 1
			idx += 1
			if idx >= len(lis):
				break

	idx = i - 1
	if idx < 0:
		b = 0
	else:
		while lis[idx] != 1 :
			b+=1
			idx-=1
			if idx < 0:
				break

	return max(a,b), min(a, b)






T = int(raw_input())



for i in range(T):

	data = raw_input().split()

	l = int(data[0])
	k = int(data[1])

	slot = [0] * l



	current_len = 0

	end = (l-1)/2
	slot[end] = 1
	k -= 1

	last_s = end

	while k > 0:
		
		
		begin = -1
		end = next_full(slot, begin)
		# print (begin , end)

		max_len = -1
		current_len_begin = -1
		current_len_end = next_full(slot, current_len_begin)
		# print (current_len_begin, current_len_end)

		while begin < end:
			
			# print (current_len_begin, current_len_end)

			current_len = end - begin - 1
			
			if current_len > max_len:
				max_len = current_len
				current_len_begin = begin
				current_len_end = end
			
			begin = end
			end = next_full(slot, end)
			# print (begin, end)


		last_s = (current_len_end + current_len_begin) / 2
		slot[last_s] = 1
		k -= 1


	# _min, _max = min_max(slot)
	_max, _min = find_max_min(slot, last_s)

	print "Case #" + str(i+1) + ": " + str(_max) + " " +  str(_min)

	# print slot
	


	