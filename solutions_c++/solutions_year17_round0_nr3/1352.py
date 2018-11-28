#include <bits/stdc++.h>
#define ll long long 
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; q++) {
		ll n, k;
		cin >> n >> k;
		map<ll, ll, greater<ll> > stage;
		if (n % 2) {
			stage[n / 2] = 2;
		}
		else {
			stage[n / 2 - 1] = 1;
			stage[n / 2] = 1;
		}
		if (k == 1) {
			if (n % 2)
				cout << "Case #" << q << ": " << n / 2 << " " << n / 2 << endl;
			else
				cout << "Case #" << q << ": " << n / 2 << " " << n / 2 - 1 << endl;
			continue;
		}
		long long counter = 1;
		while (2 * counter + 1 < k) {
			map<ll, ll, greater<ll> > temp;
			for (auto it = stage.begin(); it != stage.end(); it++) {
				ll size = it->first;
				ll count = it->second;	
				if (size % 2) {
					temp[size / 2] += stage[size] * 2;
				}
				else {
					temp[size / 2 - 1] += stage[size];
					temp[size / 2] += stage[size];
				}
			}
			stage = temp;
			counter += counter + 1;
		}
		for (auto it = stage.begin(); it != stage.end(); it++) {
			ll size = it->first;
			ll count = it->second;
			if (counter + count < k) {
				counter += count;
				continue;
			}
			if (size % 2)
				cout << "Case #" << q << ": " << size / 2 << " " << size / 2 << endl;
			else
				cout << "Case #" << q << ": " << size / 2 << " " << size / 2 - 1 << endl;
			break;
		}
	}
	return 0;
}
