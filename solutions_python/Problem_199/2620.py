# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import fileinput
def main():
	cases = 0
	curCase = 0
	f = open('flipSol','w')
	for line in fileinput.input():
		if cases == 0:
			cases = int(line)
		else:
			curCase += 1
			status = line.split(" ")[0]
			flipper = int(line.split(" ")[1])
			sol = howMany(status, flipper)
			# n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
			f.write("Case #{}: {}".format(curCase, sol) + '\n')
		# check out .format's specification for more formatting options
	f.close()

def howMany(status, flipper):
	front = 0
	back = len(status)-1
	count = 0
	while front + flipper - 1< back:
		if status[front] == '-':
			status = flip(status,front,front+flipper-1)
			count += 1
			print status, "front"
		if status[back] == '-':
			status = flip(status,back-flipper+1,back)
			count += 1
			print status, "back"
		front += 1
		back -= 1
	possible, count = checkCentre(status[front:back+1],flipper,count)
	if possible:
		return count
	return 'IMPOSSIBLE'

def checkCentre(centre,flipper,count):
	isHappy = centre[0] == '+'
	for item in centre:
		if isHappy and item == '-':
			return False, count
		if not isHappy and item == '+':
			return False, count
	if not isHappy:
		if len(centre) != flipper:
			return False, count
		else:
			count += 1
	return True, count

def flip(status,start,end):
	res = ''
	for x in range(start,end+1):
		if status[x] == '-':
			res += '+'
		else:
			res += '-'
	return status[:start] + res + status[end+1:]



if __name__ == "__main__":
	main()