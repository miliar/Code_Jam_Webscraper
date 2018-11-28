import argparse
import collections
import pdb

LawnSize = collections.namedtuple("LawnSize", ["x", "y"])


def build_lawn(input_stream):
	lawn = []
	raw_lawn_size = input_stream.readline().lstrip().rstrip().split()
	lawn_size = LawnSize(x=int(raw_lawn_size[0]), y=int(raw_lawn_size[1]))

	for x_index in xrange(0, lawn_size.x):
		line = input_stream.readline().lstrip().rstrip().split()
		lawn.append([int(line[y_index]) for y_index in xrange(0, lawn_size.y)])

	return lawn, lawn_size


def solve_lawn(lawn, lawn_size):
	def is_max_in_column(lawn, column, height):
		for line in lawn:
			if line[column] > height:
				return False
		return True

	for line in lawn:
		max_height = 100
		max_height_indexes = []
		for y_index in xrange(0, lawn_size.y):
			if line[y_index] == max_height:
				max_height_indexes.append(y_index)
			elif line[y_index] > max_height:
				max_height = line[y_index]
				max_height_indexes = []
			elif max_height == 100:
				max_height = line[y_index]
				max_height_indexes = [y_index]

		for y_index in xrange(0, lawn_size.y):
			if y_index in max_height_indexes:
				continue
			if not is_max_in_column(lawn, y_index, line[y_index]):
				return False

	return True


def build_and_solve_lawn(input_stream):
	lawn, lawn_size = build_lawn(input_stream)

	return solve_lawn(lawn, lawn_size)


def solve(input_file, output_file):
	input_stream = open(input_file, "r")
	output_stream = open(output_file, "w")

	lawns_num = int(input_stream.readline().lstrip().rstrip())
	lawns_solved = 0

	while lawns_solved < lawns_num:
		is_possible = build_and_solve_lawn(input_stream)
		if is_possible:
			answer = "YES"
		else:
			answer = "NO"
		lawns_solved = lawns_solved + 1
		output_stream.write("Case #" + str(lawns_solved) + ": " + answer + "\n")
		print "Case #" + str(lawns_solved) + ": " + answer + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--in", dest="input_file")
    parser.add_argument("--out", dest="output_file")

    args = parser.parse_args()

    solve(args.input_file, args.output_file)
