def divide2(val):
	half = val//2
	if half == val/2:
		return half
	else:
		return half+1

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

t = int(input())
cases = []
for i in range(t):
	cases.append(input())

for c in range(t):
	lenght, num_of_people = tuple([int(i) for i in cases[c].split()])
	stalls = [True] + [False] * lenght + [True]
	flength = lenght+2
	result = []
	dist_dict = {}
	curr_numb = 0
	for i in range(flength):
		if stalls[i]:
			curr_numb = i + 1
			dist_dict[curr_numb] = 0
		else:
			dist_dict[curr_numb] += 1
	for i in range(1, num_of_people+1):
		max_key = 0
		max_value = 0
		for_del = []
		for key, value in dist_dict.items():
			if value > max_value:
				max_key = key
				max_value = value
			if value == 0:
				for_del.append(key)
		for key in for_del:
			del dist_dict[key]
		change = divide2(max_value)
		pos = max_key - 1 + change
		if i == num_of_people:
			range_left = 0
			range_right = 0
			for j in range(pos-1, -1, -1):
				if stalls[j]:
					break
				else:
					range_left += 1
			for j in range(pos+1, flength):
				if stalls[j]:
					break
				else:
					range_right += 1
			result = [range_left, range_right]
		else:
			len_bef = divide2(dist_dict[max_key])
			dist_dict[max_key] = len_bef - 1
			dist_dict[pos+1] = max_value - len_bef
			stalls[pos] = True
	print("Case #{}: {} {}".format(c+1, max(result), min(result)))
		