# given A, B, 
# N = A to B
#to find cyclic permutations of N (M) such that M <= B and M > N 
#

import math;

def CheckM( M, N , A, B):
	if ((M>=A) and (M <= B ) and (M > N)) :
		return 1;
	else :
		return 0;

		
def Combination( N, R):
	""" Compute nCr """
	fa=1;
	for i in range(0,R):
		fa=fa*factorial(2);
	return (factorial(N) / fa);
	#return Cvalue;
	
def factorial(n):
    # Ensure that n is a Natural number
    n = abs(int(n))
    if n < 1: n = 1

    # Return 1!, which is 1, when n is 1
    # Otherwise, return n * (n - 1)!
    if n == 1: 
        return 1
    else: 
        return n * factorial(n - 1)

def Rotate(number,ndigit):
	""" Rotate a number by ndigits """
	digits=Digits(number); #3
	#print(digits);
	denom=10**ndigit; # 10
	#print(denom);
	remainder=number%denom;
	#print(remainder);
	numerator=number//denom
	#print (numerator);
	rotatednum=remainder*(10**(digits-ndigit)) + numerator;
	return rotatednum;
	
	
	
def Digits(number):
	""" Return digits of a number """
	digit=0;
	#print (number);	
	while (number>=1):
		number=number-(number%10);
		#print ( number);
		number=number/10;
		digit=digit+1;
	return digit;
	
#def CyclicPermutations(N):
#	print ("Digits = " + str(Digits(N)) + " Factorial " + str(Combination(Digits(N),RepeatingDigits(N) )));
		
def readLine(A,B):
	C=0
	for N in range(A,B+1):
		#print(N);
		tempList=[];
		count = 0;
		for i in range(0,Digits(N)):
			M=Rotate(N,i);
			if CheckM(M,N,A,B):
				tempList.append(M);
				#print(M);
				
				#count+=1;
				#C+=1
		#print ("Count of rotated elements of" + str(N) + " between " + str(A) + " and " + str( B) + "  = " + str(len(tempList)));
		count=len(list(set(tempList)));  ### remove duplicate elements and count only non duplicate
		C+=count;
	return C;

def main():
	myfile=open('input.txt');
	outfile=open('output.txt','w');
	TestCases=int(myfile.readline());
	for TestCase in  range(0,TestCases):
		line=myfile.readline();
		(A1,B1)=line.split();
		A=int(A1); B=int(B1);
		#A1=int(myfile.read());
		#B1=int(myfile.read());
		#print ("A = " + str(A) + " B = " + str(B));
		print ("Case #"+str(TestCase+1)+": "+str(readLine(A,B)));
		outfile.write ("Case #"+str(TestCase+1)+": "+str(readLine(A,B))+"\n");
	myfile.close();
	outfile.close();
main();