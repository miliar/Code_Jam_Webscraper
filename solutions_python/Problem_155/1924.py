

def get_number_of_friends(shyness_array):
	total_used = 0
	num_standing = 0
	for i in range(len(shyness_array)):
		if shyness_array[i] and i > num_standing:
			num_to_add = i - num_standing
			total_used += num_to_add
			num_standing += num_to_add
		num_standing += shyness_array[i]
	return total_used

def solve():
	in_str = raw_input()
	max_shyness, shyness_string = in_str.split(" ")
	shyness_array = [int(x) for x in shyness_string]

	return get_number_of_friends(shyness_array)



def main():
	num_cases = input()
	for _ in range(num_cases):
		print("Case #{}: {}".format(_ + 1,solve()))

if __name__ == '__main__':
	main()