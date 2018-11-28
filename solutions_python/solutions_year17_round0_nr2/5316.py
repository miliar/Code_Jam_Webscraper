inputList=open('B-small-attempt6.in','r')
list1=inputList.readlines()
list1 = [x.strip() for x in list1]
list1.pop(0)
print(list1)
output = open('output.txt','w')
for i in range(0,len(list1)):
	list1[i] = int(list1[i])
index =1
for i in list1:
	list2= list(str(i))
	if(i<10):
		
		output.write('Case #' + str(index)+": "+ str(i)+'\n')

	elif list2[-1]==0:
		temp = (i-1)
		output.write('Case #' + str(index)+": "+ str(temp)+'\n')

	else:
		temp = i
		tempList= list2
		tempListNew = sorted(tempList)
	
		while tempListNew != tempList:
			temp-=1
			tempList=list(str(temp))
			tempListNew=sorted(tempList)
		output.write('Case #' + str(index)+": "+ str(temp)+'\n')
	index+=1
inputList.close()
output.close()