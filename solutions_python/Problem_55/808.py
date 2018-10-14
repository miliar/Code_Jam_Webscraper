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
		e = earning(times, capacity, group_count, groups)
		o.write('Case #'+str(i+1)+': '+str(e)+'\n')
	o.close()
	f.close()
	
def earning(times, capacity, group_count, groups):
	run = 1
	index = 0
	income = 0
	while( run <= times ):
		current_size = 0
		prev_index = index
		while 1:
			if current_size + groups[index] <= capacity:
				current_size += groups[index]
				if index == group_count - 1:
					index = 0
				else:
					index += 1
			else:
				break
			if prev_index == index:
				break
		income += current_size
		run += 1
	return income
		
if __name__ == "__main__":
    process(sys.argv[1])