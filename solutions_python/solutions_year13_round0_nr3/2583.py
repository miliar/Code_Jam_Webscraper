import math

f  = open('in.txt', 'r+')
o = open("output.txt","a")
res = ""
for index,lContents in enumerate(f):
 if index > 0:
  bounds = lContents.split(" ")
  lowerBound = int(bounds[0].rstrip())
  upperBound = int(bounds[1].rstrip())
  fandss = 0
  iWord = lowerBound
  while iWord <= upperBound:
   iWordStr = str(iWord)
   if iWordStr[::-1] == iWordStr:
    #print iWordStr+" is a palindrome"
	try:
	 rootPlusOne = math.sqrt(iWord) + 1 #to check if is int
	 if rootPlusOne != int(rootPlusOne): 
	  iWord += 1
	  continue
	 rootPlusOne = int(rootPlusOne)
	 if (str(rootPlusOne-1))[::-1] == str(rootPlusOne-1):
	  fandss += 1
	except TypeError:
	 ''''''#print math.sqrt(iWord)+" is not an int"
   iWord += 1
  res += "Case #"+str(index)+": "+str(fandss)+"\n"
o.write(res)
o.close()
f.close()