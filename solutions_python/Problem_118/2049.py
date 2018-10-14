import math
import time

num = [1L,4L,9L,121L,484L,10201L,12321L,14641L,40804L,44944L,1002001L,1234321L,4008004L,100020001L,102030201L,104060401L,121242121L,123454321L,125686521L,400080004L,404090404L,10000200001L,10221412201L,12102420121L,12345654321L,40000800004L,1000002000001L,1002003002001L,1004006004001L,1020304030201L,1022325232201L,1024348434201L,1210024200121L,1212225222121L,1214428244121L,1232346432321L,1234567654321L,4000008000004L,4004009004004L]




t0 = time.time()

#A = int(math.ceil(math.sqrt(A)))
#B = int(math.floor(math.sqrt(B)))

def findHigherIndex(B):
	global num
	index = 0
	for i in num:
		if i <= B:			
			index = index+1
			#print (i,index)
		else:
			break
	return index-1
def findLowerIndex(A):
	global num
	index = 0
	for i in num:
		if i < A:			
			index = index+1
			#print (i,index)
		else:
			break
	return index

def numberOfNumbersInRange(A,B,case,lastCase):
	count = 0.0
	try:			
			with open('C-large1-0.out', 'a') as outputFile:
				#for i in xrange(A,B+1,1):
				#	if( str(i) == str(i)[::-1]):
				#		#print 'i is: ' + str(i)
				#		j = i**2
				#		#print 'j is: ' + str(j)
				#		if( str(j) == str(j)[::-1]):
				#			outputFile.write(str(j)+',')
				#			count = count+1.0
				#	perc = 100*float(i)/(B-A)
				#	if(perc%2 == 0):
				#		print '%'+str(perc)
				low = findLowerIndex(A)
				high = findHigherIndex(B)
				print 'low: ' + str(low)
				print 'high: ' + str(high)
				count = high-low+1
				outputFile.write('Case #%d: %d'%(case,count))
				if not lastCase:
					outputFile.write('\n')
						
	except:
		pass
	print count
	print 'time elapsed: %f' %(time.time()-t0)
	
if __name__ == "__main__":
	try:			
		with open('C-large1-0.out', 'w') as outputFile:
			pass
	except:
		pass
	try:			
		with open('C-large1-0.in', 'r') as inputFile:
			case = 1
			numberOfRanges = inputFile.readline()
			for range in range(int(numberOfRanges)):
				limits = inputFile.readline()
				limits  = limits.replace('\n','')
				limits = limits.split(' ')
				A =long(limits[0])
				B = long(limits[1])
				print 'numberOF Ranges'
				print numberOfRanges
				print 'case'
				print case
				lastCase = (numberOfRanges == case)
				numberOfNumbersInRange(A,B,case,lastCase)
				case = case+1

	except:
		pass





