
import sys

def parse_input(fn):
	with open(fn, "r")  as f:
		lines = f.readlines()

	nbr_inputs = int(lines[0])
	lines = lines[1:] #remove the first line because it only contains the number of inputs
	inputs = []
	for line in lines:
		sequence, k = line.split(" ")
		k = int(k)
		bin_seq = from_str_to_bin(sequence)
		inputs.append( (bin_seq, k) )

	return inputs


def parse_output(test_case, nbr_flips, out_fn):
	with open(out_fn, "a+") as out_f:
		if nbr_flips >= 0:
			out_f.write("Case #%i: %i\n" %(test_case, nbr_flips))
			return "Case #%i: %i\n" %(test_case, nbr_flips)

		else:
			out_f.write("Case #%i: IMPOSSIBLE\n" %(test_case))
			return "Case #%i: IMPOSSIBLE\n" %(test_case)



def from_str_to_bin(seq_string):
	bin_vec = []
	for char in seq_string:
		if char == "+":
			bin_vec.append(1)

		elif char == "-":
			bin_vec.append(-1)

		else:
			print "oops, this was not supposed to happen"

	return bin_vec

def check_all_happy(sequence):
	for p in sequence:
		if p < 0:
			return False

	return True

def flip(sequence, pancakes_per_flip):
	new_seq = sequence
	for p, i in zip(sequence, range(len(sequence))):
		if p == -1 and (i + pancakes_per_flip) <= len(sequence): # needs to flip it and can flip it

			end_flip = i+pancakes_per_flip
			flipped_seq = [pck * -1 for pck in sequence[i:end_flip]]
			new_seq = sequence[:i] + flipped_seq  + sequence[end_flip:]

			break

	return new_seq


def pancake_flipper(sequence, pancakes_per_flip):
	nbr_flips = 0
	if check_all_happy(sequence):
		#print "Flipped %i times!" %(nbr_flips)
		return nbr_flips # dont even know what we should return, but well, its zero here

	while not check_all_happy(sequence):
		nbr_flips += 1
		sequence = flip(sequence, pancakes_per_flip)

		if nbr_flips > 60000:
			#print " IMPOSSIBLE "
			return -1
			#break
		

	#print "Flipped %i times!" %(nbr_flips)

	return nbr_flips



def main():
	if len(sys.argv) == 2:
		fn = sys.argv[1]
		inputs = parse_input(fn)

		for inp, i in zip(inputs, range(len(inputs))):
			nbr_flips = pancake_flipper(inp[0], inp[1])

			#parse_output(i+1, nbr_flips, "p1_out.txt")

			if nbr_flips >= 0:
				print "Case #%i: %i" %(i+1, nbr_flips)

			else:
				print "Case #%i: IMPOSSIBLE" %(i+1)



	else:
		print "you forgot the file"

if __name__ == "__main__":
	main()