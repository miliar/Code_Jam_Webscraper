
def checkpalindrome(n):
	listch = list( str( n))
    	revlistch=list(listch)
	revlistch.reverse()
	#print listch
	#print revlistch
   	return listch == revlistch
		#print "plaindrome"

def buildthelist(n):
	print '[',
	for i in xrange (n+1):
		ret=checkpalindrome(i)
		if ret :
			#print i,
			ret=checkpalindrome(i*i)
			if ret:
				print i*i , 
				print "," ,
			
	print ']'
		

#buildthelist (10**7)
list1000=[0,1,4,9,121,484]  #,10201,12321,14641,40804,44944]

list107=[ 0 , 1 , 4 , 9 , 121 , 484 , 10201 , 12321 , 14641 , 40804 , 44944 , 1002001 , 1234321 , 4008004 , 100020001 , 102030201 , 104060401 , 121242121 , 123454321 , 125686521 , 400080004 , 404090404 , 10000200001 , 10221412201 , 12102420121 , 12345654321 , 40000800004 , 1000002000001 , 1002003002001 , 1004006004001 , 1020304030201 , 1022325232201 , 1024348434201 , 1210024200121 , 1212225222121 , 1214428244121 , 1232346432321 , 1234567654321 , 4000008000004 , 4004009004004]

file1 = open("sample2.txt","r")
file2 =open("output1.txt","w")
testcount=int(file1.readline())
for caseno in range(1,testcount+1):
	count=0
	nkstr=file1.readline()
	a,b=map( long,nkstr.split())
	#print a , b
	for t in list107 :
		if a <= t <= b:
			count=count+1
	print "Case #"+str(caseno)+":"+" " +str(count)
	printstr= "Case #"+str(caseno)+":"+" " +str(count)+"\n"
	file2.write(printstr)

file1.close()
file2.close()



