/*input
4
132
1000
7
111111111111111110
*/
#include <iostream>
using namespace std;

bool check_number(long long N) {
	int temp = 9;
	int prev = 11;
	while(N!=0) {
		temp = N%10;
		if (temp <= prev)
			prev = temp;
		else
			return false;
		N/=10;
	}
	return true;
}

int compute_length(long long N) {
	int count = 0;
	while(N!=0) {
		++count;
		N/=10;
	}
	return count;
}

long long generate_number(int len, int num){
	long long number = num;
	for(int i=1; i<len; ++i) {
		number *= 10;
		number += num;
	}
	return number;
}

int main(){
	int t;
	cin>>t;
	long long N;
	for(int itr=1; itr<=t; ++itr) {
		cout<<"Case #"<<itr<<": ";
		cin>>N;
		long long number, prev=-1;
		if(check_number(N) ) 
			cout<<N;
		else {
			for(long long i = N-1; i>=prev; --i) {
				if(check_number(i)) {
					cout<<i;
					break;
				}
			}	
		}
		cout<<endl;
	}
}