import sys
import re

def readData(input):
	file = open(input, "r")
	file.readline()
	data =  file.readlines()
	file.close()
	return data
	
def getTestsNo(input):
	file = open(input, "r")
	return int(file.readline().strip('\n'))

def main():
	testno = getTestsNo(sys.argv[1])
	data = readData(sys.argv[1])
	invokelen=0
	destructlen=0
	testlen=0
	#parse all the data in
	#test = data[99]
	case=0
	#if(1==1):
	for test in data:
		case+=1
		invokelist = []
		destructlist = [] 
		testlist = []
		elementlist = []
		i=0
		test = test.strip('\n')
		test = test.split(' ')
		invokelen = int(test[i])
		
		if invokelen == 0:
			i+=1
		else:
			temp = i
			while(i<(temp+invokelen)):
				i+=1
				invokelist.append(test[i])
			i+=1
		destructlen = int(test[i])
		if destructlen == 0:
			i+=1
		else:
			temp = i
			while(i<(temp+destructlen)):
				i+=1
				destructlist.append(test[i])
			i+=1	
		testlen = int(test[i])
		if testlen != 0:
			testlist = test[i+1]
		for element in testlist:
			elementlist.append(element)
			if (len(elementlist)>1):	
			#	print "invoking ", elementlist
				elementlist = invoke(invokelist, elementlist, element)
				element = elementlist[-1]
				elementlist = destruc(destructlist, elementlist, element)
		print "Case #%d:" %case, str(elementlist).replace('\'', '')				
			
def destruc(destructlist, elementlist, element):
	for des in destructlist:
		if element in des:
			count = 0
			#for ele in elementlist:
			i = len(elementlist)-2
			while(i>=0):
				ele = elementlist[i]
				if ele in des:
					#shud we delete?
					if ele == element:
						if des[0] == des[1]:
							elementlist = []
							return elementlist
					else:
						elementlist = []
						return elementlist
				i-=1
	return elementlist
		
def invoke(invokelist, elementlist, element):
	prev = elementlist[len(elementlist)-2]
	for inv in invokelist:
		if element in inv[0:2]:
			if prev in inv[0:2]:
				if element == prev:
					if inv[1] == inv[0]:
						del elementlist[-1]
						del elementlist[-1]
						elementlist.append(inv[2])
#						print "invoked"
						return elementlist
				else:
					del elementlist[-1]
					del elementlist[-1]
					elementlist.append(inv[2])
					#print prev
					#print element
#					print "invoked"
					return elementlist
	return elementlist				
		#result = list(newtestlist)
		#print result
				
			
		
			
				
		

		

			
main()
