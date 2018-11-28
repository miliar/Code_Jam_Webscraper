#include <iostream>
#include <cstdio>
#include <sstream>
using namespace std;

long long removeZeros(long long number){
	long long divisor = 1000000000000000000;
	long long process = number;

	while(!(number/divisor)) divisor /= 10;

	while(divisor){
		if(! (process / divisor)) {
			return removeZeros(number - process - 1);
		}

		process = process % divisor;
		divisor /=10;
	}

	return number;
}

long long getTidy(long long in){
	long long out = 0;
	int index = 1;
	string inS, outS = "";
	stringstream ssIn, ssOut;

	if(in < 10) return in;

	in = removeZeros(in);

	ssIn<<in; ssIn>>inS;
	for(;index<inS.size();index++){
		if(inS[index] < inS[index-1]) break;
		outS += inS[index-1];
	}
		
	if(index<inS.size()){
		outS += inS[index-1] - 1;
		for(;index<inS.size();index++) outS += '9';
	} else {
		outS += inS[index-1];
	}

	ssOut<<outS; ssOut>>out;

	return out;
}

bool tidy(long long number){
	long long divisor = 1000000000000000000;
	while(!(number/divisor)) divisor /= 10;

	int prevDigit = 0;
	while(divisor){
		if(number/divisor < prevDigit) return false;

		prevDigit = number/divisor;
		number %=divisor;
		divisor /=10;
	}

	return true;
}

int main(){
	int t;
	cin>>t;
	
	for(int tt=1;tt<=t;tt++){
		long long number;
		cin>>number;

		while(!tidy(number)){
			number = getTidy(number);
		}

		printf("Case #%d: %lld\n", tt, number);

	}

	return 0;
}