import sys


def main():


	fDataFile = open(sys.argv[1], 'r')
    #fOutputFile = open(sys.argv[2], 'w')
    #lstTestCases = []
    #lstFirstAns = []
    #lstSecondAns = []
    #lstAns = []

	#lstData = [[0]*4 for i in range(4)]
	#lstData = fDataFile.readlines()

	iTestCase = int(fDataFile.readline())
	#print iTestCase

	J = 0
	while J < iTestCase:

		iFirstAns = int(fDataFile.readline())

		for i in range(iFirstAns-1):
			fDataFile.readline()

		sRow1 = (fDataFile.readline()).strip('\n')

		for i in range(4 - iFirstAns):
			fDataFile.readline()

		iSecAns = int(fDataFile.readline())

		for i in range(iSecAns-1):
			fDataFile.readline()

		sRow2 = (fDataFile.readline()).strip('\n')

		for i in range(4 - iSecAns):
			fDataFile.readline()

		#print "#",J, "|", iFirstAns, "|", sRow1, "|", iSecAns, "|", sRow2

		lstAns = []
		lstAns = filter(lambda x: x in sRow2.split(' '), sRow1.split(' '))
		#print lstAns

		if len(lstAns) == 0:
			print "Case #%d: Volunteer cheated!" % (J+1)

		elif len(lstAns) > 1:
			print "Case #%d: Bad magician!" % (J+1)

		else:
			print"Case #%d: %s" % ((J+1), lstAns[0])


		J += 1
		#break

if __name__ == '__main__':
	main()


