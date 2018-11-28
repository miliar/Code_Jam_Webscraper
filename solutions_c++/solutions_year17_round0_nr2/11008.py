#include<stdio.h>
#include<iostream>
using namespace std;
#include<math.h>
#include<time.h>
#include<string.h>
#include<algorithm> // in C qsort(arr,N,sizeof(int),compare);
#include<stdio.h>
#include<fstream>
#include<climits>
//#include<conio.h>

bool checkAscending(long long unsigned n){

	int temp =INT_MAX;
	int digit = -1;
	while(n){
		digit = n%10;
		if(digit > temp)
			return false;
		else{
			temp = digit;
			n = n-digit;
			n /=10;
		}
	}
	return true;
}

long long unsigned bruteForceCheck(long long unsigned n){

	while(n){

		bool result = checkAscending(n);
		if(result){
			return n;
		}
		n--;
	}

}

int countDigit(long long unsigned n){
int ct = 0;
int digit ;
	while(n){
		digit = n%10;
		n = n-digit;
		n /=10;
		ct++;
		}
return ct;
	}

int findAnamoly(long long unsigned n){
       
     int digitCount = countDigit(n);
     int ct = 0;
    int temp = INT_MAX;
    int digit = -1;
	while(n){
		ct++;
		digit = n%10;
		if(digit > temp)
			return digitCount-ct;
		else{
			temp = digit;
			n = n-digit;
			n /=10;
		}
	}
	return -1;
}

long long unsigned formNumber(long long unsigned n , int index , int digit){
long long unsigned tempN=0;
long long unsigned noOfZero = 1;
if( index == -1){
   
  for(int i=0 ; i<digit ; i++){
     tempN = tempN*10+9;
  }
}else{
	digit = digit - index-1;
   for(int i=0 ; i<digit ; i++){
    noOfZero = 10*noOfZero;
     tempN = tempN*10+9;
  }
  n = n/noOfZero;
  n--;
  tempN = (n*noOfZero)+tempN;
}

return tempN;
}


long long unsigned notBruteForceCheck(long long unsigned n ){
int digitCount = countDigit(n);

    int index = findAnamoly(n);
    if(index == -1){
       return n;
    }
    // anamoly at second last digit and last digit = 0 
    if( index == (digitCount-2) && (n%10 == 0)){
       n= formNumber(  n ,-1 , digitCount-1);
    }
    else {
    	n= formNumber(n , index , digitCount);
    }

    return notBruteForceCheck(n);

}

void readFileInput(){
	fstream in("B-small-attempt1.in") ;
	ofstream out("/home/ankitesh/probB_output.txt") ;

	if(!in.is_open()){
		cout<<"\nnot able to open input file\n";
		return ;
	}
	if(!out.is_open()){
		cout<<"\nnot able to open out file \n";
		return;
	}

	long long unsigned n, result;
	int t ,ct=1;
	in >> t;

	while(t--){
		in >> n;
		result = bruteForceCheck(n);
//		result = notBruteForceCheck(n);
		out <<"Case #"<<ct<<": "<<result<<endl;
		ct++;
	}

	in.close();
	out.close();

}


int main(){
	readFileInput();
}