def get_num(num, f):

	#a = int(f.readline()[0])
	for i in range(num):
		first_row = f.readline()
	
	first_row = first_row[:len(first_row)-1]
	first_row = first_row.split(' ')
	first_row = [int(each) for each in first_row]
	first_row.sort()
	
	for i in range(4-num):
		f.readline()
		
	return first_row
	

def solve(first, second):

	if first[3] < second[0]:
		return "Volunteer cheated!"
	count = 0
	ans = []
	for each in first:
		if each in second:
			count += 1
			ans.append(each)
	if count == 0:
		return "Volunteer cheated!"
	elif count > 1:
		return "Bad magician!"
	else:
		return str(ans[0])


def main():
	f = open('A-small-attempt1.in', 'r')
	f2 = open('answer.txt', 'w')
	
	a = f.readline()
	numtest = int(a[:len(a)-1])
	print numtest
	for i in range(numtest):
		row_one = int(f.readline()[0])
		first_row = get_num(row_one, f)
		row_two = int(f.readline()[0])
		second_row = get_num(row_two, f)
		ans = solve(first_row, second_row)
		a = "Case #" + str(i+1) + ": "+ ans
		print a
		f2.write(a)
		if i != numtest-1:
			f2.write('\n')