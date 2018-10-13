def solve(trial):
	npeople = trial[1]
	peoplestanding = 0
	peopleneeded = 0
	for i in range(0, len(npeople)):
		while peoplestanding < i:
			peopleneeded = peopleneeded + 1
			peoplestanding = peoplestanding + 1
		peoplestanding = peoplestanding + int(npeople[i])
	return peopleneeded

def interpret_input(fname):
	with open(fname, 'r') as f:
		contents = f.readlines()
	ntrials = int(contents[0])
	trials = [a.split(' ') for a in contents[1:]]
	trials = [[int(a[0]), a[1].replace('\n','')] for a in trials]
	return [ntrials, trials]

def main():
	[ntrials, trials] = interpret_input('A-large.in')
	f = open('answer.out', 'w')
	for i in range(0, ntrials):
		pneeded = solve(trials[i])
		f.write('Case #' + str(i+1) + ': ' + str(pneeded) + '\n')
	f.close()

if __name__=='__main__':
	main()