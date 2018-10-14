fileName=raw_input("name of file: ")
location="C:\\Users\\le6a\\Desktop\\"
f=open(location+fileName,"r")
data=f.read()

dictionary={'y':'a','e':'o','q':'z','z':'q'}

def updateDictionary():
	inp='ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
	outp='our language is impossible to understand there are twenty six factorial possibilitiesso it is okay if you want to just give up'
	for i in range(len(inp)):
		if inp[i]!=' ' and inp[i]!='\n' and inp[i] not in dictionary:
			dictionary[inp[i]]=outp[i]


updateDictionary()

stringList=[]
def createStringList():
	sIndex=0
	s=''
	for i in range(len(data)):
		if data[i]!='\n':
			s+=data[i]
		else:
				stringList.append(s)
				s=''

def translate(coded):
	decoded=''
	for i in range(len(coded)):
		if coded[i] in dictionary:
			decoded+=dictionary[coded[i]]
		else:
			decoded+=coded[i]
	return decoded

#print translate('ejp mysljylc kd kxveddknmc re jsicpdrysi')

	
def decoder():
	#numberOfLines=int(stringList[0])
	result=[]
	for c in range(1,len(stringList)):
		result.append(translate(stringList[c]))
	return result
createStringList()

decodedList=decoder()
tt=''
for i in range(len(decodedList)):
	tt+='Case #' + str(i+1)+': '+decodedList[i]+'\n'
newf=open('C:\\Users\\le6a\\Desktop\\result.txt',"w")
newf.write(tt)	
newf.close()
raw_input()