import sys

def read_input(input):
	f = open(input)

	num_cases = int(f.readline())
	s_max_vals = []
	s_vals = []


	for i in range(num_cases):
		line_to_list = f.readline().split(' ')
		s_max_vals.append(int(line_to_list[0]))
		case_s_vals = []
		for digit in line_to_list[1].strip():
			case_s_vals.append(int(digit))
		s_vals.append(case_s_vals)
	
	return (num_cases, s_max_vals, s_vals)

# num_cases => int
# s_max_vals => [int]
# s_vals => [[int]]
def main(writer, num_cases, s_max_vals, s_vals):

	for i in range(num_cases):
		
		shyest = s_max_vals[i]
		total_standing = 0
		friends_invited = 0

		for j in range(len(s_vals[i])):
			if total_standing >= j:
				total_standing += s_vals[i][j]
			elif s_vals[i][j] > 0:
				friends_invited += j-total_standing
				total_standing += friends_invited + s_vals[i][j]

		result_str = str(friends_invited)
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

