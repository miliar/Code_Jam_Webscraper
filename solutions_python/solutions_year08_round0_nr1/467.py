from re import split
from random import randint
from string import ljust,rjust
from sys import argv

def run_file():
	if len(argv)>1:
		filename = argv[1]
	else:
		filename = 'A-large.in'
		filename = 'A-small.in'
	f=file(filename)
	program = f.readlines()
	f.close()
	line_no = 0
	program_len = len(program)
	cases_no = int(program[line_no].rstrip())
	case_no = 1
	line_no += 1
	while case_no <= cases_no:
		engines_no = int(program[line_no].rstrip())
		engine_no = 1
		line_no += 1
		engines = []
		while engine_no <= engines_no:
			engines.append(program[line_no].rstrip())
			line_no += 1
			engine_no += 1
		queries_no = int(program[line_no].rstrip())
		query_no = 1
		line_no += 1
		queries = []
		while query_no <= queries_no:
			queries.append(program[line_no].rstrip())
			line_no += 1
			query_no += 1
		print "Case #" + str(case_no) + ": " + str(analyze(engines, queries))
		case_no +=1
				
def analyze(engines, queries):
	switches = 0
	for engine in engines:
		if (queries.__contains__(engine) == False):
			return 0
	act_engine = ""
	start_index=0
	for query in queries:
		if (engines.__contains__(query)):
			if query == act_engine or start_index == 0:
				if (start_index>0):
					switches += 1
				max_index = 0
				for engine in engines:
					if (engine != query):
						try:
							index = queries.index(engine, start_index)
						except:
							index= -1
						if (index>-1):
							if (index>max_index):
								max_index = index
								act_engine = engine
						else:
							act_engine = engine
							break
		start_index += 1
	return switches

run_file()