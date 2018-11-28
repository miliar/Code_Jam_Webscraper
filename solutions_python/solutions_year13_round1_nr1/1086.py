import sys
import shlex

f = open('small.in', 'r')
g = open('small.out', 'w')

T = int(f.readline())
test_num = 0

def main():
	global test_num
	
	for sets in range(T):
		test_num = sets
		input_vars = str.strip(f.readline()).split(' ')
		
		r = int(input_vars[0])
		t = int(input_vars[1])
		
		first_area = r**2
		second_area = (r + 1)**2
		paint_used = second_area - first_area
		
		num_rings = 0
		
		while t >= paint_used:
			t -= paint_used
			num_rings += 1
			paint_used += 4
		
		print_answer(num_rings)
		
	f.close()
	g.close()
	sys.exit()

	
def print_answer(answer):
	g.write("Case #" + str(test_num + 1) + ": " + str(answer) + "\n")
	return
	
	
main()