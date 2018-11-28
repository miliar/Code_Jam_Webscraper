#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;

typedef pair<ll, ll> ii;

int main() {
#ifdef _DEBUG
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		ll k, n;

		cin >> n >> k;

		map<ll, ll> m;
		m[n] = 1;

		ll a, b;
		while (k > 0) {
			ii z = *m.rbegin();
			m.erase(z.first);
			a = (z.first - 1) / 2;
			b = z.first - 1 - a;

			m[a] += z.second;
			m[b] += z.second;
			k -= z.second;
		}

		cout << max(a, b) << ' ' << min(a, b) << endl;
	}
	return 0;
}