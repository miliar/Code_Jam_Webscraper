import sys

def makeRowFloat(list) :
	#print ("makeRowFloat")    
	#print ("original eachRow : ",eachRow)
	eachRowFloat = [float(x) for x in list]
	print ("---------------------------Float eachRowFloat : ",eachRowFloat)
	return eachRowFloat
def currentFarmToWin (toWinCookies, cookiesPerSec) :
	secTimeWinWithFarm = toWinCookies/cookiesPerSec
	#print ("secTime cookie per sec: ",secTimeWinWithFarm)
	return secTimeWinWithFarm
def toBuyFarm(farmPrice, cookiesPerSec) :
	sTimeToBuyNewFarm = farmPrice / cookiesPerSec
	#print ("secTime to buy farm cookie per sec: ",sTimeToBuyNewFarm)
	return sTimeToBuyNewFarm

#print ("start program")
txt = "B-small-attempt0.in"

infile = open(txt,'r')
count = 0

caseCount = 0
sPla = ''
LastString = ''
for line in infile :
	#print("line : ",line)
	if count == 0 :
		lCase = line.split()
		#print ("lCase  ------------------------- : ",lCase)
		sCase = lCase[0]
		numCase = int(sCase)
		#print ("numCase ------------------------ : ",numCase)
	if count >= 1 :
		data = line.split()
		#print("data : ",data)
		dataFloat = makeRowFloat(data) 
		compareResult = []
		farm = 0
		timeBuyEachFarm = []
		cookiePerSec = 0
		noFarmSecTime = dataFloat[2]/2
		#noFarmSecTime = noFarm(dataFloat[2])
		compareResult.append(noFarmSecTime)
		#print("compareResult : ",compareResult)
		while True :
			if farm == 0 :
				sTimeToBuy1st = toBuyFarm(dataFloat[0],2)
				timeBuyEachFarm.append(sTimeToBuy1st)
				cookiePerSec = 2 + dataFloat[1]
				time = currentFarmToWin(dataFloat[2],cookiePerSec)
				sTimeWith1stFarm = time + sum(timeBuyEachFarm)
				compareResult.append(sTimeWith1stFarm)
				##print("compareResult : ",compareResult)
				farm = farm + 1
				if compareResult[-2] < sTimeWith1stFarm :
					print("in if")
					break						 
			elif  farm > 0:
				##print ("more farm")
				sTimeToBuy = toBuyFarm(dataFloat[0],cookiePerSec)
				timeBuyEachFarm.append(sTimeToBuy)
				##print("timeBuyEachFarm : ",timeBuyEachFarm)
				cookiePerSec = cookiePerSec + dataFloat[1]
				time = currentFarmToWin(dataFloat[2],cookiePerSec)
				sTimeWithMoreFarm = time + sum(timeBuyEachFarm)
				##print("sTimeWithMoreFarm : ",sTimeWithMoreFarm)
				compareResult.append(sTimeWithMoreFarm)
				##print("compareResult : ",compareResult)
				farm = farm + 1                 
				if compareResult[-2] < sTimeWithMoreFarm :
					print("in if")
					break
			else :
				print ("000000")
		##print("sTimeWithMoreFarm : ",sTimeWithMoreFarm)            
		##print("compareResult : ",compareResult)
		sPla = 'Case #'+str(count)+": "+str(compareResult[-2])+'\n'
		##print ("sPla : ",sPla)
		LastString = LastString + sPla
		print (LastString)
	count = count + 1
	#print (count," : count")
	
fo = open("B-cookie-Small-output.out", "w")
fo.write(LastString);
#close opend file
fo.close()
	
				 
