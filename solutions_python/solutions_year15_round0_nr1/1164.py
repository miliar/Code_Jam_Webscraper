def solve(effectif):
	invite= 0
	gens_debout= 0
	max_shyness = len(effectif)
	for cur_shyness in range(max_shyness):
		if(gens_debout < cur_shyness):
			invite += cur_shyness -gens_debout
			gens_debout = cur_shyness + effectif[cur_shyness]
		else:
			gens_debout += effectif[cur_shyness]
	return invite

def parse_cases(filename):
	fhandle = open(filename)
	lines = fhandle.readlines()
	curline = 0
	nb_cases = int(lines[curline])
	curline +=1
	finished = False
	outfile = open("outfile.out", 'w')
	while(not(curline>=nb_cases+1)):
		line = lines[curline].split()
		print line
		effectif = map(int , line[1])
		effectif = map(int, list(effectif))
		curline+=1
		solution = solve(effectif)
		print "Case #%d: %d" %(curline, solution)
		outfile.write("Case #%d: %d\n" %(curline-1, solution))
	fhandle.close
	outfile.close

# effectif = '110011'
# effectif = map(int, list(effectif))
# print effectif
# print solve(effectif)

parse_cases('A-large.in')