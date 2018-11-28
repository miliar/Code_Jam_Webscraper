# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import fileinput
def main():
	cases = 0
	curCase = 0
	f = open('tidySol','w')
	for line in fileinput.input():
		if cases == 0:
			cases = int(line)
		else:
			curCase += 1
			n = str(line.strip())
			sol = lastTidy(n)
			f.write("Case #{}: {}".format(curCase, sol) + '\n')
		# check out .format's specification for more formatting options
	f.close()

def lastTidy(n):
	subCarry = False
	# curInt = int(n[len(n)-1])
	# nextInt = int(n[len(n)-2])
	# if curInt < nextInt or curInt == 0:
	# 	curInt = 9
	# 	subCarry = True
	# n = n[:len(n)-1] + str(curInt)
	for x in range(len(n)-1,0,-1):
		curInt = int(n[x])
		nextInt = int(n[x-1])
		if subCarry:
			if curInt == 0:
				curInt = 9
				n = nineOut(n,x, len(n))
			else:
				curInt -= 1
				subCarry = False
		if curInt < nextInt or curInt == 0:
			curInt = 9
			n = nineOut(n,x, len(n))
			subCarry = True
		n = n[:x] + str(curInt) + n[x+1:]
	if subCarry and n[0] == '1':
		return n[1:]
	if subCarry:
		n = str(int(n[0])-1) + n[1:]
	return n

def nineOut(s1, x, length):
	return s1[:x+1] + '9'*(length-x-1)

if __name__ == "__main__":
	main()