/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>            
#define ll long long
#define ld double
#define mp make_pair

using namespace std;

const double PI = 3.14159265358979323846;
const ll maxn = (ll)401;
const ll maxlog = (ll)13;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e9 + 7;
const ld eps = 1e-7;

ll n, m, t, x, p, a[maxn], it[maxn];
vector<vector<ll> > v(maxn);

ll getk(ll x, ll y) {
	if ((10 * x) % (11 * y) == 0) 
		return 10 * x / (11 * y);
	else
		return 10 * x / (11 * y) + 1;
}

ll getri(ll x, ll y) {
	return 10 * x / (y * 9) + 1;
}

bool f(ll x, ll k, ll y) {
	if (abs(y * k - x) * 10 <= y * k) {
		return true;
	}
	return false;
}

ll getkk(ll x, ll y) {
	ll tk = x / y;
	for (ll k = max(1ll, tk - 5); k <= tk + 5; k++) {
		if (abs(k * y - x) * 10 <= k * y) {
			return k;
		}
	}
	return -1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (ll ii = 0; ii < t; ii++) {
		cin >> n >> p;
		memset(it, 0, sizeof it);
		for (ll i = 0; i < n; i++) {
			v[i].clear();
		}
		for (ll i = 0; i < n; i++) {
			cin >> a[i];
		}
		for (ll i = 0; i < n; i++) {
			for (ll j = 0; j < p; j++) {
				cin >> x;
				ll tk = getk(x, a[i]);
				if (tk != -1) {
					v[i].push_back(x);
				}
			}
		}
		for (ll i = 0; i < n; i++) {
			sort(v[i].begin(), v[i].end());
		}
		ll ans = 0;
		while (true) {
			bool can = true;
			ll mi = inf;
			ll mii = inf;
			ll ma = 0;
			for (ll i = 0; i < n; i++) {
				if (it[i] == v[i].size()) {
					can = false;
					break;
				}
				ll tk = getk(v[i][it[i]], a[i]);
				ll ri = getri(v[i][it[i]], a[i]);
				if (i == 0) {
					ma = ri;
					mi = tk;
				}
				else {
					mi = max(mi, tk);
					ma = min(ma, ri);
				}
			}
			if (!can) {
				break;
			}
			can = false;
			for (int j = mi; j <= ma; j++) {
				bool tcan = true;
				for (ll i = 0; i < n; i++) {
					mii = min(mii, getk(v[i][it[i]], a[i]));
					if (!f(v[i][it[i]], j, a[i])) {
						tcan = false;
					}
				}
				if (tcan) {
					can = true;
					break;
				}
			}
			if (mi > ma) {
				for (ll i = 0; i < n; i++) {
					mii = min(mii, getk(v[i][it[i]], a[i]));
				}
			}
			if (can) {
				ans++;
				for (ll i = 0; i < n; i++) {
					it[i]++;
				}
			}
			else {
				for (ll i = 0; i < n; i++) {
					if (getk(v[i][it[i]], a[i]) == mii) {
						it[i]++;
					}
				}
			}
		}
		memset(it, 0, sizeof it);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < v[i].size(); j++) {
				if (getkk(v[i][j], a[i]) == 1) {
					swap(v[i].back(), v[i][j]);
					v[i].pop_back();
					j--;
				}
			}
		}
		for (ll i = 0; i < n; i++) {
			sort(v[i].begin(), v[i].end());
		}
		ll ans1 = 0;
		while (true) {
			bool can = true;
			ll mi = inf;
			ll ma = 0;
			for (ll i = 0; i < n; i++) {
				if (it[i] == v[i].size()) {
					can = false;
					break;
				}
				ll tk = getkk(v[i][it[i]], a[i]);
				ma = max(ma, tk);
			}
			if (!can) {
				break;
			}
			for (ll i = 0; i < n; i++) {
				if (!f(v[i][it[i]], ma, a[i])) {
					it[i]++;
					can = false;
				}
			}
			if (can) {
				ans1++;
				for (ll i = 0; i < n; i++) {
					it[i]++;
				}
			}
		}
		printf("Case #%lld: %lld\n", ii + 1, max(ans1, ans));
	}
	return 0;
}