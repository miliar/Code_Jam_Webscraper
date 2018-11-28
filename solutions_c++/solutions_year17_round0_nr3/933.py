#include <bits/stdc++.h>
using namespace std;

void gettl(bool b) {
	int crt = 1;
	if (!b) {
		for (int i = 0; i < (int) 2e9; i++) {
			crt *= 17;
		}
		gettl(false);
	}
}

#ifndef _DEBUG
#define ass(_Expr) ((void)0)
#define dout(...) ((void)0)
#else
#define dout(...) cout << __VA_ARGS__; cout.flush()
#define ass(_Expr) assert(_Expr);
#endif

typedef long long ll;
typedef double ld;
const int INF = 2e9;
const ll LINF = 2e18;
const ll MOD = 1e9 + 9;
const int PRIME = 29;
const ld EPS = 1e-10;
const ld PI = 3.14159265358979323846;

pair<ll, ll> getdiv(ll k) {
	if (k & 1) {
		return {k >> 1, k >> 1};
	} else {
		return {k >> 1, (k >> 1) - 1};
	}
}

void solve() {
	ll n, k;
	cin >> n >> k;
	map<ll, ll> ams;
	ams[n] = 1;
	int iter = 0;
	while (k) {
		iter++;
		auto big = ams.end();
		big--;
		auto res = getdiv(big->first);
		if (big->second >= k) {
			cout << res.first << " " << res.second << "\n";
//			cerr << iter << " iterations for " << n << "\n";
			return;
		} else {
			k -= big->second;
			ams[res.first] += big->second;
			ams[res.second] += big->second;
			ams.erase(big);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
//	freopen("keepcounted.in", "r", stdin);
//	freopen("keepcounted.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		cout << "CASE #" << tt + 1 << ": ";
		solve();
	}
	return 0;
}
