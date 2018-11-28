import copy 

def find_possible_triples(scores):
	l = []
	for score in scores:
		res = []
		for i in range(0,11):
			for j in range(0,11):
				for k in range(0,11):
					if i + j + k == score:
						t = sorted([i, j, k])
						if t[2] - t[0] <= 2 and t not in res:
							res.append(t)
		new_l = []
		for new_score in res:
			if len(l) == 0:
				new_l.append([new_score])
			else:
				for prev_score in l:
					prev = copy.deepcopy(prev_score)
					prev.append(new_score)
					new_l.append(prev)
		l = new_l
	return l

def has_surprising(triples, s):
	"See if a a set of scores have s surprising scores"
	count = 0
	for triple in triples:
		if triple[2] - triple[0] == 2:
			count += 1
	return count == s

def find_count(triples, p):
	"Count number of scores in a set of scores that are greater than or equal to p"
	return len([triple for triple in triples if triple[2] >= p])

def find_max_count(possible_triples, p, s):
	"Find the maximum count of p given a set of possible triples"
	max = 0
	for t in possible_triples:
		temp = find_count(t, p)
		if temp > max:
			max = temp
	return max

if __name__ == "__main__":
	input = file("B-small.in").read().strip().split('\n')
	output = open("B-small.out", "w")

	cases = int(input[0])
	for i in range(0, cases):
		line = input[i+1].split()
		num_googlers = int(line[0])
		num_surprising = int(line[1])
		p = int(line[2])
		scores = [int(score) for score in line[3:]]
		possible = [scores for scores in find_possible_triples(scores) if has_surprising(scores, num_surprising)]
		count = find_max_count(possible, p, num_surprising)
		output.write("Case #{0}: {1}\n".format(i+1, count))
	output.close()
