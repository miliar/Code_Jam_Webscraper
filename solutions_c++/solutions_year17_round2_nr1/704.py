#include <iostream>
using namespace std;


typedef long long ll;


void test_case(){
	ll d, n;
	cin >> d >> n;
	ll num = 1;
	ll den = 0;
	for(int i=1; i<=n; i++){
		ll k,s; cin >> k >> s;
		if(s*den < (d-k)*num){
			num = s;
			den = d-k;
		}
	}
	cout << (double)d*num/den << endl;
}

int main(){
	cout.precision(10);
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		test_case();
	}
	return 0;
}
