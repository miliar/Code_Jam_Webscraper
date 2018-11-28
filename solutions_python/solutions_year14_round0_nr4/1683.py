import sys

def ken(lstKen, fNaomiBlock):

	lstOptions = filter(lambda x: x > fNaomiBlock, lstKen)

	if len(lstOptions) == 0:
		return min(lstKen)
	else:
		return min(lstOptions)


def D_naomi(lstNaomi, lstKen):

	maxOfKen = max(lstKen)
	minOfKen = min(lstKen)
	lstChoose = filter(lambda x: x > minOfKen, lstNaomi)
	lstChoose.sort()
	#print lstChoose

	if len(lstChoose) > 0:
		return {'tell':float(maxOfKen+0.01), 'choose':lstChoose[0]}
	else:

		return {'tell':lstNaomi[0], 'choose':lstNaomi[0]}



def main():

	fDataFile = open(sys.argv[1], 'r')
	lstData = fDataFile.readlines()
	iTestCases = int(lstData[0])

	#print fData
	iIndex = 1

	for iTest in range(iTestCases):

		iNaomiPoints = 0
		iDeciNaomiPoints = 0
		iCount = int(lstData[iIndex])
		iIndex +=1
		sNaomi = lstData[iIndex]
		lstNaomi = map(float, sNaomi.split(' '))
		iIndex +=1
		sKen = lstData[iIndex]
		lstKen = map(float, sKen.split(' '))
		iIndex +=1

		#print lstNaomi
		#print lstKen
		lstKen_1 =list(lstKen)
		lstNaomi_1 = list(lstNaomi)

		for iAttemp in range(iCount):

			dictNaomi = D_naomi(lstNaomi, lstKen)
			fKen_block = ken(lstKen, dictNaomi['tell'])

			#print dictNaomi

			if dictNaomi['choose'] > fKen_block:

				iDeciNaomiPoints += 1

			lstKen.remove(fKen_block)
			lstNaomi.remove(dictNaomi['choose'])

		#print lstKen1

		for iAttemp in range(iCount):

			fNaomi_block = max(lstNaomi_1)
			fKen_block = ken(lstKen_1, fNaomi_block)

			if fNaomi_block > fKen_block:
				iNaomiPoints += 1

			lstKen_1.remove(fKen_block)
			lstNaomi_1.remove(fNaomi_block)




		print "Case #%d: %d %d" % ((iTest+1), iDeciNaomiPoints, iNaomiPoints)





if __name__ == '__main__':
	main()


