#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>

#define mp make_pair
#define pb push_back


typedef long long ll;
typedef long double ld;

using namespace std;

#ifndef LOCAL
#define cerr _cer
struct _cert
{
    template <typename T> _cert& operator << (T) { return *this; }
};
_cert _cer;
#endif

template <typename T> void dprint(T begin, T end) {
    for (auto i = begin; i != end; i++) {
		cerr << (*i) << " ";
    }
    cerr << "\n";
}

map<ll, ll> mm;
ll n, k;

void solve() {
	scanf("%lld%lld", &n, &k);
	mm.clear();
	mm[n] = 1;
	--k;
	while (k) {
		pair<ll, ll> now = *mm.rbegin();
		ll go = min(k, now.second);
		if (now.second == go)
			mm.erase(now.first);
		else
			mm[now.first] -= go;
		k -= go;
		ll l = (now.first - 1) / 2;
		ll r = (now.first - 1) - l;
		if (l != 0)
			mm[l] += go;
		if (r != 0)
			mm[r] += go;
	}
	ll now = mm.rbegin()->first;
	ll l = (now - 1) / 2;
	ll r = (now - 1) - l;
	cout << r << " " << l << "\n";
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}


