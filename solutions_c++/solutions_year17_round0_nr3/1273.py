#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

typedef long long ll;

int t, tbk;

int main() {
	ll n, k;
	cin >> t;
	tbk = t;
	while (t) {
		t--;
		cout << "Case #" << tbk - t << ": ";
		cin >> n >> k;
		ll x, m, r;
		for (ll i = 0;;i++) {
			if (!(k >> i)) {
				x = i - 1;
				break;
			}
		}
		k -= ((ll)1 << x) - 1;
		m = (n - (((ll)1 << x) -1)) / ((ll)1 << x);
		r = (n - (((ll)1 << x) -1)) % ((ll)1 << x);
		if (k > r) {
			cout << m / 2 << ' ' << (m - 1) / 2 << endl;
		} else {
			cout << (m + 1) / 2 << ' ' << m / 2 << endl;
		}
	}
}
