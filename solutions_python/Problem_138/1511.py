fo = fo = open("D-large.in","r+")
fw = open("output.txt","w")
def ToInt(str):
	return int(str.strip())

def kenOptimalPlay(n, kenPiecies):
	for l in range(0,len(kenPiecies)):
		if n < kenPiecies[l]:
			return kenPiecies[l]
		else:
			continue

	return kenPiecies[0]

def Deceive(n, kenPiecies):
	if n < min(kenPiecies):
		return max(kenPiecies) - 0.0001
	else:
		return max(kenPiecies) + 0.0001


count = ToInt(fo.readline())

for i in range(1,count+1):
	naomiScore = 0
	kenScore = 0
	fo.readline()
	naomiPiecies = [float(j) for j in fo.readline().strip().split()]
	kenPiecies = [float(j) for j in fo.readline().strip().split()]
	naomiPiecies.sort()
	kenPiecies.sort()
	
	deceifulkenPiecies = list(kenPiecies)
	deceifulNaomiScore = 0
	deceifulKenScore = 0

	for j in range(0,len(naomiPiecies)):
		kenOptimal = kenOptimalPlay(naomiPiecies[j], kenPiecies)
		naomiTell = Deceive(naomiPiecies[j], deceifulkenPiecies)
		
		kenDeceivedOptimal = kenOptimalPlay(naomiTell , deceifulkenPiecies)


		if naomiPiecies[j] < kenOptimal:
			kenScore = kenScore +1
		else :
			naomiScore = naomiScore + 1
		kenPiecies.remove(kenOptimal)


		if naomiPiecies[j] < kenDeceivedOptimal:
			deceifulKenScore = deceifulKenScore +1
		else :
			deceifulNaomiScore = deceifulNaomiScore + 1
		deceifulkenPiecies.remove(kenDeceivedOptimal)

	fw.write("Case #{0}: {1} {2}\n".format(i,deceifulNaomiScore, naomiScore))

fo.close()
fw.close()
