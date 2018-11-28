#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define X first
#define Y second

#define debug(a) cerr << #a << " = " << (a) << endl;

template<typename T> ostream& operator<<(ostream& o, const vector<T>& v) {
	for (const auto& a : v) o << a << " ";
	return o;
}

/*
map<ll, map<ll, pll>> dp;

pll recurse(ll n, ll k) {
	if (dp[n].count(k)) {
		return dp[n][k];
	}
	// ok we allocate the first guy. so we'll split into (n/2) and (n - 1 - (n/2))
	ll a = n/2;
	ll b = n - 1 - a;
	if (a == b) {
		// now we'd go to the LEFT first, then right
		return recurse(a, (k-1)/2);
	} else {
		// now we'd go to the RIGHT first, then left
	}
}
*/

ll helper(ll n, ll k) {
	map<ll, ll> segments;
	segments[n] = 1;

	while (true) {
		const auto cur = segments.rbegin();
		const ll size = cur->first;
		const ll count = cur->second;

		if (k - count <= 0) {
			return size;
		}
		k -= count;
		// split!
		ll a = size / 2;
		ll b = size - 1 - a;
		segments[a] += count;
		segments[b] += count;

		// erase last!
		auto z = segments.end();
		z--;
		segments.erase(z);
	}
	return -1;
}

pll do_case() {
	ll n, k;
	cin >> n >> k;
	ll size = helper(n, k);
	ll a = size / 2;
	ll b = size - 1 - a;
	return {a, b};
}

int main() {
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		const auto ans = do_case();
		cout << "Case #" << (c+1) << ": " << ans.X << " "  << ans.Y << endl;
	}
}
