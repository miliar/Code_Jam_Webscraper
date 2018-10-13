"""
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
"""
import string
import math

def CheckABC(A,B,C):
	""" Check the Triplets are not crossing 2 border """
	print ("A = " + str(A) + "B = " + str(B) + " C = " + str(C));
	if (A < 0 or B < 0 or C < 0 ):
		#print "A,B,C < 0";
		return 1;
	else:
		return 0;
		
	if ( A > 10 or B > 10 or C > 10 ):
		return 1;
	else:
		return 0;
		
	#abs(a-b), abs (a-c), abs (b-a) , abs (b-c) is always < 2
	if ((abs(a-b) > 2 )  or (abs(a-c) > 2 ) or (abs(c-b) > 2 )) :
		return 1;
	else:
		return 0;

def BestResult(A,B,C):
	return max(A,B,C);

def surpriseSplit( TS, surprise, P ):
	bestcount=0
	S=surprise
	
	for score in TS:
		#print (score);
		a=b=c=score/3;
#		if (a >= P):
#			score-=P;
#			a=P;
#			if (score%2==0):
#				b=c=score/2;
#			else:
#				b=(score-1/2);
#				c=(score-1)/2+1;
#			print ("Checkabc = " + str(CheckABC(a,b,c)))
#			if (CheckABC(a,b,c)==0):
#				print (score/2, score/2, P)
#		else:

		if (score%3==0):
			a=b=c=score/3;
		#	print (score/3, score/3, score/3);
			# check if we have single value greater than P
			if ((a <P) and (a+1 >= P) and S>0 and c>0):
				a=a+1; 
				c=c-1;
				S=S-1;
		elif (score%3==1):  # 433  423 5
			c=b=(score-1)/3; a=c+1;
		#	if ((a <P)and (a+1 >= P) and c>0 and ):
		#		if (S>0):
		#			a=a+1; 
		#			b=b-1;
		#			S=S-1; ## difference is 2
			#elif ((a <P)and (a+2 >= P)):
			#	a=a+2;
			#	c=c-1;
			#	b=b-1;
			#elif ((a <P)and (a+4 >= P)):
			#	a+=4;
			#	c-=2;
			#	c-=2;
			#	S=S-1; ## use a surprise
			
		#	print ((score-1)/3, (score-1)/3, (score-1)/3+1)
		elif (score%3==2): # 11 , 5,   3,4,4
			
			a=(score-2)/3; b=a+1; c=a+1;
			if (c<P and c+1==P and S>0):
				b=a; c=a+2; S=S-1;
		#	print ((score-2)/3, (score-2)/3, (score-2)/3+2)
		#print (a,b,c, S);
		if(BestResult(a,b,c) >= P): 
			bestcount+=1;
	#print ("BR = " + str(bestcount));
	return bestcount;

def ReadInputFile():
	InputFile=open("input.txt")
	# Read Firstline for Total Testcases
	TestCases=InputFile.readline()
	#print("Number of Testcases = " + TestCases )
	if (int(TestCases) > 100 ):
		print ("Number of Testcases greater than 100")
	# Read Total Dancers Lines
	for TestCase in range(int(TestCases)):
		myArray = [ int(x) for x in InputFile.readline().split() ]
		Dancers=myArray[0]
		Surprises=myArray[1]
		P=myArray[2]
		TotalScores=myArray[3:]
		#print ("======= TESTCASE " + str(TestCase) + "==============")
		#print ("Number of Dancers   = " + str(Dancers))
		#print ("Number of Surprises = " + str(Surprises))
		#if (Surprises > Dancers):
		#	print ("No of Surprises greater than No of Dancers")
		#print ("Number of value P   = " + str(P))
		#print (' '.join(map(str,TotalScores)))
		print ("Case  #"+str(TestCase+1)+": "+str(surpriseSplit(TotalScores, Surprises, P )))

#def WriteOutputFile(TC, Result)
#	for TestCase in range(TC):
#		print ("Case #"+TestCase+": "+int(Result[TC]))

ReadInputFile()