



f = open('A-small-attempt0.in', 'r')
wf = open('A-small-attempt0.out', 'w')

def doCase(case):
	realrow = int(f.readline())
	for i in range(1, 5):
		if realrow == i:
			square= [int(n) for n in f.readline().split()]
			continue
		f.readline()
	secondrow = int(f.readline())
	for i in range(1, 5):
		if secondrow == i:
			rearrange = [int(n) for n in f.readline().split()]
			continue
		f.readline()
	same = 0
	number = 0
	for i in square:
		for j in rearrange:
			if i == j:
				same += 1
				number = i
	if same == 0 and number == 0:
		wf.write('Case #{}: Volunteer cheated!\n'.format(case))
	if same > 1:
		wf.write('Case #{}: Bad magician!\n'.format(case))
	if same == 1:
		wf.write('Case #{}: {}\n'.format(case, number))
				




def main():
	N = int(f.readline())
	for i in range(1, N+1):
		doCase(i)
	f.close()
	wf.close()




if __name__ == '__main__':
	main()