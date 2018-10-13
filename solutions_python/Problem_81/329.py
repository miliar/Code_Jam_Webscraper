import os
import copy

def read_vector_str(s):
	return [i for i in s.split(" ")]

def read_vector_int(s, vector_length):
	vector = []
	index_start = 0
	for _ in xrange(0, vector_length-1): 
		index_end = s.find(" ", index_start)
		vector.append(int(s[index_start:index_end]))
		index_start = index_end + 1
	vector.append(int(s[index_start:]))
	return vector

def calc_wp(record):
	games = 0.0
	wins = 0.0
	for ch in record:
		if (ch == "0"):
			games += 1.0
		if (ch == "1"):
			games += 1.0
			wins += 1.0

	if (games > 0): return wins/games
	return 0


def calc_owp(record, team):
	owp = 0.0
	opponents = 0.0
	#for r in record:
	for j in xrange(0, len(record)):
		if (j == team) or (record[j][team] == "."): continue
		opponents += 1.0
		games = 0.0
		wins = 0.0
		for i in xrange(0, len(record[j])):
			if (i == team): continue
			if (record[j][i] == "0"):
				games += 1.0
			if (record[j][i] == "1"):
				games += 1.0
				wins += 1.0
		if (games > 0): owp += wins/games
	
	
	if (opponents > 0): return owp/opponents
	return 0


def calc_oowp(record, OWP, team):
	oowp = 0.0
	opponents = 0.0
	for i in xrange(0, len(OWP)):
		if (record[i][team] == "."): continue
		if not(i == team):
			oowp += OWP[i]
			opponents += 1
			
	if (opponents > 0): return oowp/opponents
	return 0

filepath = "/home/mike/Downloads/"
filename = "A-large"

f_in = open(os.path.join(filepath, filename+".in"), "rb")
f_out = open(os.path.join(filepath, filename+".out"), "wb")
num_test_cases = int(f_in.readline())

for test_case in xrange(1, num_test_cases+1):
#for test_case in xrange(1, 5):
	N = int(f_in.readline())
	record = []
	for team in xrange(0, N):
		record.append(f_in.readline())


	WP = []
	OWP = []
	for team in xrange(0, N):
		WP.append(calc_wp(record[team]))
		OWP.append(calc_owp(record, team))

	OOWP = []
	for team in xrange(0, N):
		OOWP.append(calc_oowp(record, OWP, team))

	RPI = []
	for team in xrange(0, N):
		RPI.append(0.25 * WP[team] + 0.5 * OWP[team] + 0.25 * OOWP[team]) 

#	print WP
#	print OWP
#	print OOWP
#	print RPI
		
	#output = "Case #%d: %s" % (test_case, ("Broken", "Possible")[possible])
	f_out.write("Case #%d:\n" % (test_case))
	for rpi in RPI:
		f_out.write("%s\n" % (rpi))
	#f_out.write(output+"\n")

f_out.close()