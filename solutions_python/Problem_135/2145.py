filename = "A-small-attempt0.in"

def perform_magic_trick(positions, arrangements):
	possible_chosen_values_before = set(arrangements[positions[0]-1])
	possible_chosen_values_after = set(arrangements[positions[1]+3])
	result = list(possible_chosen_values_before.intersection(possible_chosen_values_after))
	if len(result) == 0:
		return "Volunteer cheated!"
	elif len(result) == 1:
		return repr(result[0])
	else:
		return "Bad magician!"


def main(t, fin, fout):
	preliminary_text = "Case #%s: "
	for i in xrange(t):
		pos = []
		arrangement = []
		line = fin.readline()
		pos.append(int(line.strip()))
		for j in xrange(4):
			line = fin.readline()
			arrangement.append(map(int, line.split()))
		line = fin.readline()
		pos.append(int(line.strip()))
		for j in xrange(4):
			line = fin.readline()
			arrangement.append(map(int, line.split()))
		result = perform_magic_trick(pos, arrangement)
		fout.write(preliminary_text %(i+1))
		fout.write(result + "\n") 

if __name__ == "__main__":
	fin = open(filename, "r")
	fout = open("output.txt", "w")	
	line = fin.readline()
	t = int(line.strip())
	main(t, fin, fout)
	fin.close()
	fout.close()