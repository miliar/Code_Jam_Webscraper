import re
import string
import sets

basefilename = 'A-small'
infilename = basefilename+'-attempt0.in'
outfilename = basefilename+'.out'

strfrom = 'acbedgfihkjmlonqpsrutwvyxz'
strto = 'yehosvcdxiulgkbzrntjwfpamq' 

def main():
	# Utils
	resultlist = []
	N = 0

	# Take input
	infile = open(infilename, 'Ur')
	N = int(infile.readline())
	casenum = 0
	for line in infile:
		# DO IT
		casenum += 1
		letters = sets.Set([letter for letter in line])
		resultline = line
		resultline = resultline.translate(string.maketrans(strfrom, strto)) 
		resultlist.append("Case #" + str(casenum) + ": " + resultline)

	# Write output	
	outfile = open(outfilename, 'w')
	outfile.writelines(resultlist)

	# Lets close this
	infile.close()
	outfile.close()

if __name__ == "__main__":
	main()

