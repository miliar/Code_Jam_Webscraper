#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int T,ct,i,max_digit;
	long long int N,t;
	long long int adder[19];

	adder[0] = 1;
	for(i=1;i<=17;i++)
		adder[i] = adder[i-1]*10+1;

	cin >> T;
	for (ct = 1; ct <= T; ++ct) {
		cin >> N;
		if(N<10){
			cout << "Case #" << ct << ": " << N << endl;
			continue;
		}
		if(N==10){
			cout << "Case #" << ct << ": 9" << endl;
			continue;
		}
		t = 0; max_digit = 0;
		for(i=17;i>=0;i--){
			while(t+adder[i]<=N){
				t = t+adder[i];
				max_digit++;
				if(max_digit==9)
					break;
			}
			if(max_digit==9)
				break;
		}
		cout << "Case #" << ct << ": " <<t<< endl;
	}
}