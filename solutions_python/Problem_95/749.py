# usage a.py <infile> > outfile
import sys

infile = sys.argv[1]

english = "aozurlngeismpbtdhwyxfckjvq"
googlerese = "yeqjpmslckdxvnribtahwfougz"

mapping = dict()
for g, e in zip(googlerese, english):
	mapping[g] = e

f = open(infile, "r")

T = (int) (f.readline().strip())

for t in range(1, T+1):
	line = f.readline().strip()
	output = ""
	for letter in line:
		if letter in mapping:
			output += mapping[letter]
		else:
			output += letter
	print ("Case #" + str(t) + ": " + output)
	
f.close()
