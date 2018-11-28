#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
	int T;
	cin >> T;
	ll n, k;
	for(int t = 1; t <= T; t++) {
		cin >> n >> k;
		ll i = 1;
		while(i <= k) {
			i *= 2;
		}
		i /= 2;
		ll res = (n + i - k) / i; 
		// cout << "res = " << res << " i = " << i << endl;
		cout << "Case #" << t << ": " << res/2  << " " << (res - 1)/2 << endl; 
	}
}