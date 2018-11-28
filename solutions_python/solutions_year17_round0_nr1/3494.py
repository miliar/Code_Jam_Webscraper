import sys
import codecs
import io

def main():
	count = 0
	sys.stdout = codecs.getwriter('utf8')(sys.stdout)
	num_testcases = int(sys.stdin.readline().rstrip())
	outfile = open('large_output.txt', 'w')
	
	while (count < num_testcases):
		line = sys.stdin.readline().rstrip()
		splitline = line.split();
		pannenkoeken = splitline[0]
		flipper_width = int(splitline[1])
		#print('Starting case')
		output = happy_side_up(pannenkoeken, flipper_width, count+1)
		outfile.write(output)
		count += 1

def happy_side_up(pancakes, flipper_width, case):
	startindex = 0
	endindex = len(pancakes) - flipper_width;
	num_flips = 0
	
	while (startindex <= endindex):
		if (pancakes[startindex] == '-'):
			#print('Flipping')
			pancakes = flip(pancakes, startindex, flipper_width)
			num_flips += 1
		startindex += 1	
	
	#print('End state: ' + pancakes)
	
	if (check_happy(pancakes)):
		success = 'Case #' + str(case) + ': ' + str(num_flips) + '\n'
		return success
	else:
		failure = 'Case #' + str(case) + ': IMPOSSIBLE\n'
		return failure
		
def flip(pancakes, index, width):
	charlist = list(pancakes)
	#print('index: ' + str(index))
	
	for i in range(index, index+width):
		#print('i: ' + str(i))
		#print('Before replace: ' + "".join(charlist))
		if(charlist[i] == '-'):
			charlist[i] = '+'
		else:
			charlist[i] = '-'
		#print('After replace : ' + "".join(charlist))
	
	return "".join(charlist)
	
def check_happy(pancakes):
	if (pancakes.rfind('-') == -1):
		return True
	else:
		return False
		
if __name__ =='__main__':main()
