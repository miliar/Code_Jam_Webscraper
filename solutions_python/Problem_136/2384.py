import sys

def time_taken(c, f, x):
	increment = 2
	current_num = 0
	time_taken = 0
	while(current_num < x):
		if(x - current_num <= c):
			time_taken += (x-current_num)/ increment
			current_num = x
		else:
			time_taken += c/increment
			current_num += c

			time_at_current_rate = (x-current_num)/increment
			time_at_new_rate = (x)/(increment + f)

			if(time_at_new_rate < time_at_current_rate):
				current_num = 0
				increment += f
	return time_taken

def process_case(num):
	c, f, x = raw_input().split(' ')
	c = float(c)
	f = float(f)
	x = float(x)
	sys.stdout.write('Case #' + str(num + 1) + ': ' + str(time_taken(c, f, x)) + '\n')

def main():
	t = input()
	i = 0
	while i < t:
		process_case(i)
		i += 1
	
main()





