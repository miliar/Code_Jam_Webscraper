import csv

count = 1
length = 0
data = []

with open('3_in.txt', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter= ' ')
	for row in reader:
	    if count == 1:
	    	length = row[0]
	    else:
	    	data.append(row)
	    count += 1



case_num = 0
status = ''
for row in data:
	case_num += 1
	arr = [int(row[0])]
	for i in range(0, int(row[1])):
		max_val = max(arr)
		if i == int(row[1]) - 1:
			if max_val % 2 == 0:
				status += "Case #" + str(case_num) + ": " + str(max_val/2) + " " + str(max_val/2 - 1) + '\n'
			else:
				status += "Case #" + str(case_num) + ": " + str((max_val - 1)/2) + " " + str((max_val - 1)/2) + '\n'
			break
		arr.remove(max_val)
		if max_val % 2 == 0:
			arr.append(max_val/2)
			arr.append(max_val/2 - 1)
		else:
			arr.append((max_val - 1)/2)
			arr.append((max_val - 1)/2)
			
with open('3_out.txt', 'w') as out:
	out.write(status)