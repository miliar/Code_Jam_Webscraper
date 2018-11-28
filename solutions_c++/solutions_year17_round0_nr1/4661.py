#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

long long tidy(long long x) {

	if(x<10) return x;
	long long base = 10;

	long long digit = floor(log10(x)),first_digit = 0;

	while(digit>0) {
		long long first,second; 
		first = x/(long long)pow(base,digit); 
		first = first%10;
		second = x/(long long)pow(base,digit-1);
		second = second%10;


		if(first>second) {
			long long mo;
			if(first_digit != 0) mo = pow(10,first_digit);
			else mo = pow(10,digit) ;
			return x-x%mo-1;
		}
		else if(first == second && first_digit == 0) first_digit = digit;
		digit--;

	}
	return x;

}

int pancake(string s, int x) {

	int i=0,count=0; 
	for(; i<s.size()-x; i++) {
		if(s[i] == '-') {
			count++;
			for(int j=i; j<i+x; j++) {
				s[j] = s[j]=='-' ? '+' : '-';
			}
		}

	}
	char cur = s[i];

	for(; i<s.size(); i++) {
		if(s[i] != cur) return -1;
	}
	if(cur == '-') count++;
	

	return count;

}


int main() {
	ifstream myfile;
	ofstream output;
	myfile.open("A-large.in");
	output.open("output.out");
	
	int n;
	myfile >> n;

	for(int i=0; i<n; i++) {
		string s;
		int x;
		myfile >> s >> x;
		//cout<<s<<" "<<x<<":"<<pancake(s,x)<<endl;
		if(pancake(s,x) == -1) 
			output<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		else output << "Case #"<<i+1<<": "<<pancake(s,x)<<endl;
	}

	output.close();
	myfile.close();
	return 0;

}
