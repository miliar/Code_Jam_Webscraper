#include <iostream>
#include <math.h>
using namespace std;
typedef long long ll;

int at(ll x, int i) {
	i = log10(x) - i;
	return fmod(x/pow(10,i),10);
}

int main() {
	int t;
	cin >> t;
	for (int tc=1; tc<=t; tc++) {
		ll x;
		cin >> x;
		int tidy = 0;
		
		while (!tidy) {
			tidy = 1;
			ll n = log10(x);
			for (int i=0; i<n; i++) {
				if (at(x,i)>at(x,i+1)) {
					x = x-fmod(x,pow(10,n-i))-1;
					tidy = 0;
					break;
				}
			}
		}
		cout << "Case #" << tc << ": " << x << endl;
	}
	return 0;
}