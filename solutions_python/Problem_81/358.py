import sys

def main() :
	lines = sys.stdin.readlines()
	cases = int(lines[0])
	count = 1
	for case in xrange(cases) :
		n = int(lines[count])
		count = count + 1
		result = [[0 for i in xrange(n)] for j in xrange(n)]
		numwins = [0] * n
		numplays = [0] * n
		wp = [0.0] * n
		owp = [0.0] * n
		oowp = [0.0] * n
		rpi = [0.0] * n
		for i in xrange(n) :
			line = lines[count]
			wins = 0
			plays = 0
			count = count + 1
			for j in xrange(n) :
				if line[j] == '.' :
					result[i][j] = -1
				else :
					plays = plays + 1
					if line[j] == '0' :
						result[i][j] = 0
					else :
						result[i][j] = 1
						wins = wins + 1
			numwins[i] = wins
			numplays[i] = plays
			wp[i] = (wins*1.0)/plays
		for i in xrange(n) :
			owpTemp = 0.0
			for j in xrange(n) :
				if result[i][j] != -1 :
					if result[i][j] == 1 :
						owpTemp += (numwins[j] * 1.0) / (numplays[j] - 1)
					else :
						owpTemp += ((numwins[j]-1) * 1.0) / (numplays[j] - 1)
			owp[i] = owpTemp / numplays[i]
		for i in xrange(n) :
			oowptemp = 0.0
			for j in xrange(n) :
				if result[i][j] != -1 :
					oowptemp += owp[j]
			oowp[i] = oowptemp / numplays[i]
		print "Case #" + str(case+1) + ":"
		for i in xrange(n) :
			print (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i])
		

main()
