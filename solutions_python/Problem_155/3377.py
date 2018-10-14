def add_audience(max, audience):
	min_invited = 0
	cur_standing = int(audience[0])
	for i in range(1,max+1):
		if(cur_standing + min_invited < i):
			while min_invited + cur_standing < i:
				min_invited += 1
		cur_standing += int(audience[i])
	return min_invited

inputf = open('A-large.in')
outputf = open('output-large.txt', 'a')
num = inputf.readline()
for i in range(0, int(num)):
	temp = inputf.readline().split()
	outputf.write("Case #" + str(i+1) + ": " + str(add_audience(int(temp[0]), temp[1])) + "\n")

outputf.close()
inputf.close()