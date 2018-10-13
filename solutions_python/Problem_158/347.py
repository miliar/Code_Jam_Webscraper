import sys

def read_input(input):
	f = open(input)

	num_cases = int(f.readline())
	x_vals = []
	r_vals = []
	c_vals = []

	for i in range(num_cases):
		line_list = f.readline().split(" ")
		x_vals.append(int(line_list[0]))
		r_vals.append(int(line_list[1])) 
		c_vals.append(int(line_list[2])) 
	
	return (num_cases, x_vals, r_vals, c_vals)

# num_cases => int
# x_vals => [int]
# r_vals => [int]
# c_vals => [int]
def main(writer, num_cases, x_vals, r_vals, c_vals):

	for i in range(num_cases):

		x = x_vals[i]
		r = r_vals[i]
		c = c_vals[i]

		winner = "RICHARD"
		if (r*c) % x == 0:
			if (x < 3 or (x == 3 and r*c >= 6) or (x == 4 and r*c >= 12)):
				winner = "GABRIEL"

		result_str = winner
		writer.write_output(i, result_str)

	return

class Writer():

	def __init__(self):
		self.output = open('outputs/' + sys.argv[1].split('/')[1][:-2] + 'out', 
						   'w+')
	
	def write_output(self, iteration_num, result_str):
		result_base = "Case #"+str(iteration_num+1)+": "
		self.output.write(result_base+result_str+'\n')

if __name__ == "__main__":
	formatted_input = read_input(sys.argv[1])
	w = Writer()
	main(w, *formatted_input)
	w.output.close()

