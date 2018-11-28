#include <bits/stdc++.h>
#define ll long long
using namespace std;
void solve() {
	ll k,n;
	cin >> n >> k;
	map<ll,ll> M;
	M[n] = 1;
	while (1) {
		ll cnt = M.rbegin()->second;
		ll len = M.rbegin()->first;
		if (cnt >= k) {
			cout << len/2 << " " << (len-1)/2 << endl;
			return;
		}
		M.erase(len);
		M[len/2] += cnt;
		M[(len-1)/2] += cnt;
		k -= cnt;
	}
	return;
}
int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
	return 0;
}