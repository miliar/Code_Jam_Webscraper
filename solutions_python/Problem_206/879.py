file1 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Round 1_b/horse_input_large.in','r')
file2 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Round 1_b/horse_output_large.txt','w')

cases = file1.readline()
counter = 0
for line in file1:
	counter += 1
	total_dist, num_horses = line.split()
	total_dist = int(total_dist)
	num_horses = int(num_horses)
	times = [0] * num_horses
	for i in range(num_horses):
		init_dist, speed = file1.readline().split()
		times[i] = (total_dist - int(init_dist))/int(speed)
	max_speed = max(times)

	file2.write("Case #" + str(counter) + ": " + str(total_dist/max_speed) + "\n")

file1.close()
file2.close()
