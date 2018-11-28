'''
Created on May 9, 2010

@author: indra
'''
import sys, os

filename = "C-large"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

ncases = int(reader.readline().rstrip())

caseno = 0
while caseno<ncases:
	caseno+=1
	case = reader.readline().rstrip()
	R,k,N = [int(x) for x in case.split(' ')]
	case = reader.readline().rstrip()
	gps = [int(x) for x in case.split(' ')]
	totp = 0
	for gp in gps:
		totp+=gp
	print (R,k,N)
	print gps
	print totp
	
	if totp<=k:
		writer.write("Case #%s: %d\n" % (str(caseno),R*totp))
		continue
	
	rides = [-1]*N
	money = [0]*N
	
	retmon = 0
	
	curloc = 0
	curride = 0
	curmon = 0
	while rides[curloc]==-1 and curride<R:
		rides[curloc] = curride
		money[curloc] = curmon
		curride+=1
		tem=0
		while tem+gps[curloc]<=k:
			tem+=gps[curloc]
			curloc+=1
			if curloc>=N:
				curloc-=N
		curmon+=tem
		
	if curride==R:
		writer.write("Case #%s: %d\n" % (str(caseno),curmon))
		continue
	
	cycrides = curride - rides[curloc]
	cycmoney = curmon - money[curloc]
	
	R-=rides[curloc]
	retmon+=money[curloc]
	
	rleft = R%cycrides
	retmon += cycmoney*((R-rleft)/cycrides)
	
	lastrides = 0
	while lastrides<rleft:
		lastrides+=1
		tem=0
		while tem+gps[curloc]<=k:
			tem+=gps[curloc]
			curloc+=1
			if curloc>=N:
				curloc-=N
		retmon+=tem
	writer.write("Case #%s: %d\n" % (str(caseno),retmon))
writer.close()