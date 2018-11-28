def str2set(s):
	return set([int(i) for i in s.split()])

def getRow():
	rowNum = int(input())
	for i in range(rowNum - 1):
		input()
	row = str2set(input())
	for i in range(4 - rowNum):
		input()
	return row
		
def solver():
	row1 = getRow()
	row2 = getRow()
	return row1 & row2

def main():
	t = int(input())
	for i in range(1, t + 1):
		number = solver()
		print("Case #{:d}: {:s}".format(i, str(number.pop()) if len(number) == 1 else "Volunteer cheated!" if len(number) == 0 else "Bad magician!"))

if __name__ == "__main__":
	main()