# Pancake Flip
# Google CodeJam - 2017 - Qualification Round - Problem A
# Author: Daniel Ruland

import helper

def flip_pancakes(pancakes, size):
	stack = pancakes
	height = len(stack)
	print "height: %s" % height # debug
	
	flips = 0
	
	while True:
		# if all +'s, we're done
		if stack.find('-') == -1:
			return flips
	
		# If flipper is too big, case is impossible (unless already correct)
		if size > height:
			return "IMPOSSIBLE"
	
		# create an empty stack for our arrangement after we flip
		# also increment flip now since we know we're flipping
		new_stack = ""
		flips += 1
		
		# find our flip location
		index_end = stack.rfind("-") + 1
		index_start = index_end - size
		
		# if we overshoot end of stack, it means combo is impossible
		if index_start < 0:
			return "IMPOSSIBLE"
		
		# if we're not all the way left, start building our new stack up to the 
		# beginning of the flip
		if index_start != 0:
			new_stack += stack[:index_start]
		
		# add our flipped pancakes to the stack
		for p in stack[index_start:index_end]:
			if p == "-":
				new_stack += "+"
			else:
				new_stack += "-"
				
		# add the rest off the original stack if we're not alredy all the way right
		if index_end < height:
			new_stack += stack[index_end:]
		
		# finally, reset our stack for the next iteration
		stack = new_stack
		print stack #debug
		
def test():
	dataset = helper.get_dataset()
	outfile = helper.create_output_file()
	num = 1
	
	for case in dataset:
		data = case.split(" ")
		pancakes = data[0]
		size = int(data[1])
		
		print flip_pancakes(pancakes, size)
				

def main():
	dataset = helper.get_dataset()
	outfile = helper.create_output_file()
	num = 1
	
	for case in dataset:
		data = case.split(" ")
		pancakes = data[0]
		size = int(data[1])
		
		solution = flip_pancakes(pancakes, size)
		
		outfile.write("Case #" + str(num) + ": " + str(solution) + "\n")
		print "Case #%s: %s" % (num, solution)
		num += 1
	
	outfile.close()
	print "[+] All cases solved!"
	
if __name__=='__main__':
	main()
