import sys, os

def process(filename):
	print filename
	f = open(filename, 'r')
	o = open(filename.split('.')[0]+'.out', 'w+')
	count = int(f.readline())
	for i in range(count):
		s = f.readline().split(' ')
		times = int(s[0])
		capacity = int(s[1])
		group_count = int(s[2])
		groups = [int(c) for c in f.readline().split(' ')]
		
		e = new_earning(times, capacity, group_count, groups)
		o.write('Case #'+str(i+1)+': '+str(e)+'\n')
		print i
	o.close()
	f.close()

def new_earning(times, capacity, group_count, groups, init_index = 0):
	array = prepare_data(groups)
	flags = [(-1,0) for i in range(group_count)]
	run = 1
	index = init_index
	flags[0] = (0,0)
	earning = 0
	while run <= times:
		next_index, fill  =  fill_current(index, capacity, array)
		#print str(next_index) + "--" + str(fill)
		if flags[next_index][0] != -1:
			prev_run = flags[next_index][0]
			prev_earn = flags[next_index][1]
			
			remaining_run = times - prev_run
			
			run_diff = run-prev_run
			run_earn = ( earning + fill )- flags[next_index][1]
			
			loop_earn = (remaining_run / run_diff)*run_earn
			#print str(run) + '-' + str(next_index)
			return (prev_earn + loop_earn + new_earning(remaining_run % run_diff, capacity, group_count, groups,next_index))
		else:
			earning += fill
			flags[next_index] = (run, earning)
			index = next_index
			run += 1
	return earning
		
def fill_current(index, capacity, array):
	ret = 0
	size = len(array[index])
	traverse = range(size)
	traverse.reverse()
	for i in traverse:
		if array[index][i] <= capacity:
			return (index + (i+1)) % size, array[index][i]
			
	return 0, 0
			
	
def prepare_data(groups):
	data = []
	for i in range(len(groups)):
		l = get_sum(groups, i)
		data.append(l)
	return data
		
def get_sum(l, index):
	new_l = [i for i in l]
	new_l.extend(new_l)
	new_list = []
	sum = 0
	count = 0
	while count < len(l):
		sum += new_l[index]
		new_list.append(sum)
		index += 1
		count += 1
	return new_list

def earning(times, capacity, group_count, groups):
	run = 1
	index = 0
	income = 0
	broken = 0
	len = group_count -1
	while run <= times:
		current_size = 0
		prev_index = index
		while 1:
			new_size = current_size + groups[index]
			if current_size + groups[index] <= capacity:
				current_size = new_size
				if index == len:
					index = 0
				else:
					index += 1
			else:
				break
			if prev_index == index:
				break
		income += current_size
		
		if index == 0:
			broken = 1
			break
		else:
			run += 1
	
	if broken == 1:
		remaining = times%run
		factor = times/run
		return income*factor + earning(remaining, capacity, group_count, groups)
	else:
		return income
		
if __name__ == "__main__":
    process(sys.argv[1])