#include <iostream>
#include <cmath>

#define ll long long

using namespace std;

ll len(ll n){
	ll result = 1;
	while(1){
		n /= 10;
		if(0 == n) break;
		result++;
	}
	return result;
}

int main(){
	int tests;
	cin >> tests;
	for(int i=0; i<tests; i++){
		ll n;
		cin >> n;
		bool finished = false;
		while(1){
			ll laenge = len(n);
			int akt = 0;
			int j=0;
			ll c = 0;
			while(1){
				c = n/pow(10.0, laenge-1-j);
				c %= 10;
				if(akt > c) break;
				akt = c;
				if(j == laenge-1) finished = true;
				if(j == laenge-1) break;
				j++;
			}
			if(finished) break;
			ll temp = pow(10.0, laenge-j);
			ll minus = n % temp;
			minus++;
			n -= minus;
		}
		cout << "Case #" << i+1 << ": " << n << endl;
	}
}
