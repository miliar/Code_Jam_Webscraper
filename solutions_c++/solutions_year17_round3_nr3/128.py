#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> llp;

const ll INF = 1000000000000;
const ld eps = 1e-8;

int main() {
	ll t;
	cin >> t;

	for (ll q = 0; q < t; q++) {
		cout << "Case #" << q + 1 << ": ";

		ll n, k;
		cin >> n >> k;
		ld u;
		cin >> u;
		multiset<ld> p;
		for (ll i = 0; i < n; i++) {
			ld x;
			cin >> x;
			p.insert(x);
		}

		ll c = 1;
		ld v = *p.begin();
		p.erase(p.begin());
		
		while (!p.empty() && abs(*p.begin() - v) < eps) {
			c++;
			p.erase(p.begin());
		}
 
		while (u > eps && !p.empty()) {
			ld d = *p.begin() - v;
			d = min(d, u / c);

			v += d;
			u -= d * c;

			while (!p.empty() && abs(*p.begin() - v) < eps) {
				c++;
				p.erase(p.begin());
			}
		}

		if (u > eps) {
			v += u / c;
		}

		ld ans = 1;
		for (ll i = 0; i < c; i++) {
			ans *= v;
		}

		while (!p.empty()) {
			ans *= *p.begin();
			p.erase(p.begin());
		}

		cout << setprecision(8) << fixed << ans << "\n";
	}

	return 0;
}