#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define mp make_pair
#define f first
#define s second
#define ld long double
#define pb push_back

const ll MAXN = 1e18;

inline void solve() {
	ll n, k;
	cin >> n >> k;
	--k;
	set<pair<ll, ll> > Q;
	map<ll, ll> am;
	am[n] = 1;
	Q.insert(mp(-n, 1));
	for (ll i = 0; i < k; ++i) {
		//cerr << Q.size() << endl;
		auto v = *Q.begin();
		Q.erase(v);
		ll temp = min(k - i, v.s);
		//cerr << temp << endl;
		am[-v.f] -= temp;
		if (am[-v.f] != 0) {
			Q.insert(mp(v.f, am[-v.f]));
		}
		v.f *= -1;
		//cerr << v.f << ' ' << v.s << ' ' << i << ' ' << temp << endl;
		--v.f;
		ll a, b;
		a = b = v.f / 2;
		if (v.f % 2) ++a;
		Q.erase(mp(-a, am[a]));
		am[a] += temp;
		am[a] = min(am[a], MAXN);
		Q.insert(mp(-a, am[a]));
		Q.erase(mp(-b, am[b]));
		am[b] += temp;
		am[b] = min(am[b], MAXN);
		Q.insert(mp(-b, am[b]));
		i += temp - 1;
	}
	auto v = *Q.begin();
	Q.erase(v);
	--am[-v.f];
	if (am[-v.f] != 0) {
		Q.insert(mp(v.f, am[-v.f]));
	}
	v.f *= -1;
	--v.f;
	ll a, b;
	a = b = v.f / 2;
	if (v.f % 2) ++a;
	cout << a << ' ' << b;
}

int main() {
    freopen("gcj.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		//cerr << i << endl;
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
}
