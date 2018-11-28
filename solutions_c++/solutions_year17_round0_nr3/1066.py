#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

typedef long long ll;

vector<ll> pw;

int main() {
	ll cur = 1ll;
	for (int i = 0; i < 64; i++) {
		pw.push_back(cur);
		cur *= 2ll;
	}
	int tt; cin >> tt;
	for (int t = 1; t <= tt; t++) {
		ll k, n; cin >> k >> n;
		ll g = *(--upper_bound(pw.begin(), pw.end(), n));
		ll z = (k-n)/g;
		cout << "Case #" << t << ": " << z/2 + z%2 << ' ' << z/2 << '\n';
	}
}