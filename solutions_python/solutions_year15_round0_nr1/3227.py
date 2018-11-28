def calc_friends(values,case):
	temp = list(values)
	current = 0
	friends = 0
	index=0
	if "0" in temp:
		for i in temp:
			current +=int(i)
			if(current<(index+1)):
				diff = (index+1)-current
				friends+=diff
				current+=diff
			index+=1
	else:
		friends = 0
	result_string = "Case #{}: {}"
	print result_string.format(case, friends)
			
if __name__ == '__main__':
	f=open('inputs/A-large.in','r')
	n = int(f.readline())
	i=1
	for line in f:
		data = line.split( )
		smax = data[0]
		values = data[1]
		calc_friends(values,i)
		i+=1

