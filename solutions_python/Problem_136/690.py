import string

input = open('B-large.in', 'r')
out = open('B-large.out', 'w')

n = int(input.readline())
for count in range(n):
	c, f, x = [float(s) for s in string.split(input.readline(), ' ')]
	speed = 2
	total_time = 0
	while True:
		if x/speed > c/speed+x/(speed+f):
			total_time += c/speed
			speed += f
		else:
			total_time += x/speed
			break
	out.write('Case #'+str(count+1)+': '+str(total_time)+'\n')
	# print('Case #'+str(count+1)+': '+str(total_time))