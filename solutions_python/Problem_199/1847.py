#GCJ 2017
#oversized pancake flipper

INFILE = "A-large.in"
OUTFILE = "A-large.out"

def get_flips(S, K):
	flips = 0
	S_list = []
	for cake in S:
		S_list.append(cake)
	for i, cake in enumerate(S_list):
		if cake == "-":
			if i+K <= len(S):
				for j in range(K):
					if S_list[i+j] == "-":
						S_list[i+j] = "+"
					else:
						S_list[i+j] = "-"
				flips  += 1
	if S_list.count("-") == 0:
		return flips
	else:
		return "IMPOSSIBLE"
		
fin = open(INFILE, "r")
fout = open(OUTFILE, "w")

num = fin.readline()
for case in range(int(num)):
	line = fin.readline()
	S, K = line.split()
	fout.write("Case #" + str(case + 1) + ": ")
	fout.write(str(get_flips(S, int(K))) + "\n")
	
fin.close()
fout.close()
