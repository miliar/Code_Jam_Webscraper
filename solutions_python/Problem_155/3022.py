"""
Problem A. Standing Ovation
A_description.txt
A.input
A.output
"""
import sys

output_file = 'A.output'

class StandingOvation():

	def __init__(self):
		pass

	def run(self, filename):
		result = []
		with open(filename, 'r') as f:	
			n_test_cases = [int(num) for num in f.readline().split()][0]
			for n_case in range(1,n_test_cases+1):
				s_max, s_kth = [num for num in f.readline().split()]
				s_kth_lst = [int(num) for num in list(s_kth)]
				result.append("Case #%s: %s" % (n_case, self.calculate_missing(int(s_max), s_kth_lst)))
		self.write_to_file(result)

	def calculate_missing(self, s_max, s_kth_lst):
		stand = 0
		count = 0
		for index in range(0,s_max + 1):
			if(stand < index):
				count += 1
				stand += 1
			stand += s_kth_lst[index]
		return count

	def write_to_file(self, result):
		with open(output_file, 'w') as f:
			f.write('\n'.join(result))


if __name__ == '__main__':
	
	standing_ovation = StandingOvation()
	standing_ovation.run(sys.argv[1])