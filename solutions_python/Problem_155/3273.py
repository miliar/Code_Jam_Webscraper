#/usr/bin/python

import datetime
import sys

if __name__ == "__main__":

	inputFile = sys.argv[1]

	with open(inputFile, "r") as file:
		inp = file.read().splitlines()

	T = inp[0]

	with open(inputFile.replace(".in", ".out"), "a") as outputFile:

		for i in range(1,len(inp)):
			Smax = inp[i].split(" ")[0]
			case = inp[i].split(" ")[1]

			inf_audience = 0
			invited = 0
			S=0


			for nb in case:
				nb = int(nb)
				while S > inf_audience + invited:
					invited += 1
				inf_audience += nb
				S += 1

				if inf_audience + invited >= Smax:
					break

			outputFile.write("Case #" + str(i) + ": " + str(invited) + "\n") 
