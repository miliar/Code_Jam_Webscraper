#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
#include <ctime>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

long long int locate(long long int N,long long int K){
	long long int t,num;
	long long int lo,hi,nl,nh;
	if(K==1) return N;
	
	lo = (N-1)/2; hi = N/2;
	nl = 1; nh = 1;
	K--; num = 2;
	while(K > num){
		if(lo==hi){
			nl*=2;
			nh*=2;
		}
		else {
			if(lo%2==0)
				nh = nh*2+nl;
			else
				nl = nl*2+nh;
		}
		lo = (lo-1)/2;
		hi = hi/2;
		K-=num; num*=2;
	}

	if(K <= nh)
		t = hi;
	else
		t = lo;

	return t;
}

void main() {
	int T,ct,i,j;
	long long int N,K,t;
	long long int max_d,min_d;

	cin >> T;
	for (ct = 1; ct <= T; ++ct) {
		cin >> N; cin >> K;
		if(K==N || N==1){
			cout << "Case #" << ct << ": 0 0"<< endl;
			continue;
		}

		t = locate(N,K);
		//odd: 2m+1 -> (m,m)
		//even:  2m -> (m,m-1)
		max_d = t/2;
		min_d = (t-1)/2;

		cout << "Case #" << ct << ": " <<max_d<<" "<<min_d<< endl;
	
	}
}