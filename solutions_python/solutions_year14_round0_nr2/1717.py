import sys


def get_farm(C, Rate, F, X):

	fSecFarm = float(C / Rate)
	fComplete = X / float(Rate+F) + fSecFarm

	return {'totsec':fComplete, 'farmsec': fSecFarm}

def main():

	fDataFile = open(sys.argv[1], 'r')
	#iTestCases = int(fDataFile.readline())
	i_CurrentRate = 2
	f_CookieSec = 0.0
	i_Count = 0

	fData = fDataFile.readlines()
	#print fData

	for sLine in fData[1:]:

		i_Count += 1
		lstSec = []
		i_CurrentRate = 2
		sFeilds = sLine.split(' ')
		C = float(sFeilds[0])
		F = float(sFeilds[1])
		X = float(sFeilds[2])

		#print C, F, X

		fCurrentSec = X / i_CurrentRate
		dictNextFarm = get_farm(C, i_CurrentRate, F, X)
		fNxtFarmSec = dictNextFarm['totsec']

		#print fCurrentSec, "|", fNxtFarmSec

		while fCurrentSec > fNxtFarmSec:

			#print fCurrentSec, "||", fNxtFarmSec

			i_CurrentRate = i_CurrentRate + F
			lstSec.append(dictNextFarm['farmsec'])

			fCurrentSec = X / i_CurrentRate + sum(lstSec)

			#Get farm
			##################
			fSecFarm = float(C / i_CurrentRate)
			fComplete = X / float(i_CurrentRate+F) + fSecFarm
			dictNextFarm = {'totsec':fComplete, 'farmsec': fSecFarm}
			##################

			#dictNextFarm = get_farm(C, i_CurrentRate, F, X)
			fNxtFarmSec = dictNextFarm['totsec'] + sum(lstSec)


		print "Case #%d: %.7f" % (i_Count, fCurrentSec)





if __name__ == '__main__':
	main()


