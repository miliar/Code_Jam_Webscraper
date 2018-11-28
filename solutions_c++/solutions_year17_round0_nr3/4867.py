#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve() {
	int n, k;
	cin >> n >> k;
	map<ll, ll> active;
	ll biggest = 0;
	active[n] = 1;
	while (k > 0) {
		biggest = active.rbegin()->first;
		k -= active[biggest];
		active[(biggest - 1)/2] += active[biggest];
		active[biggest/2] += active[biggest];
		active.erase(biggest);
	}
	cout << biggest/2 << " " << (biggest - 1)/2; 
}

int main() {
	int t;
	cin >> t;
	for (int i=1; i <=t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}