import sys

def read_input(input):
	f = open(input)

	num_cases = int(f.readline())
	num_diners_vals = []
	pancakes_vals = []

	for i in range(num_cases):
		num_diners_vals.append(int(f.readline()))
		pancakes_to_diners = f.readline().split(' ')
		pancakes_vals.append([int(pancakes) for pancakes in pancakes_to_diners])	
	
	return (num_cases, num_diners_vals, pancakes_vals)

# num_cases => int
# num_diners_vals => [int]
# pancakes_vals => [[int]]
def main(writer, num_cases, num_diners_vals, pancakes_vals):

	for i in range(num_cases):
		
		pancakes_dist = pancakes_vals[i]
		current_time = 0
		solution_times = []
		starting_max_pancakes = max(pancakes_dist)

		solve(pancakes_dist, solution_times, starting_max_pancakes, current_time)

		result_str = str(min(solution_times))
		writer.write_output(i, result_str)

	return

def solve(pancakes_dist, solution_times, starting_max_pancakes, current_time):

	if current_time >= starting_max_pancakes:
		return

	max_pancakes = max(pancakes_dist)

	# How long we'll take if we consume all pancakes w/o further moves
	solution_times.append(max_pancakes+current_time)

	# Move the tall stack and recurse
	most_pancakes = pancakes_dist.index(max_pancakes)
	for j in range(2, max_pancakes/2+1):
		next_pancakes = pancakes_dist[:]
		next_pancakes[most_pancakes] -= j
		next_pancakes.append(j)
		solve(next_pancakes, solution_times, 
			starting_max_pancakes, current_time+1)
	
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

# while current_time <= starting_max_pancakes:
# 			max_pancakes = max(pancakes_dist)

# 			# How long we'll take if we consume all pancakes w/o further moves
# 			solution_times.append(max_pancakes+current_time)

# 			# Move the tall stack and iterate
# 			most_pancakes = pancakes_dist.index(max_pancakes)
# 			pancakes_to_move = max_pancakes/2

# 			pancakes_dist[most_pancakes] -= pancakes_to_move
# 			pancakes_dist.append(pancakes_to_move)

# 			current_time += 1
