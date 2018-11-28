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



void stall_minmax(long long stall, long long people, long long& min_val, long long& max_val) {

	if(people == 0) {
		min_val = stall;
		max_val = stall;
	}
	else if(people == 1) {
		min_val = (stall-1)/2;
		max_val = stall/2;
	}
	else {
		if(people%2 == 1) stall_minmax((stall-1)/2, (people-1)/2, min_val, max_val);
		else stall_minmax(stall/2, people/2, min_val, max_val);
	}
}


int main() {
	ifstream myfile;
	ofstream output;
	myfile.open("C-large.in");
	output.open("output.out");
	
	int n;
	myfile >> n;
	for(int i=0; i<n; i++) {
		long long stall, people, min_val=-1, max_val=-1;
		myfile >> stall >> people;
		stall_minmax(stall, people, min_val, max_val);
		//cout<<"max: "<<max_val<<", min: "<<min_val<<endl;
		output<<"Case #"<<i+1<<": "<<max_val<<" "<<min_val<<endl;
	}

	output.close();
	myfile.close();
	return 0;

}
