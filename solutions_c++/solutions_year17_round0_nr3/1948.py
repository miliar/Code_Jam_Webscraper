#ifdef LOCAL
#include "locallibs.h"
#else
#include <bits/stdc++.h>
#endif

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;


pair<ll, ll> brute(ll n, ll k)
{
	map<ll, ll> s;
	s[n] = 1;
	
	while (k > 0)
	{
		ll biggest = s.rbegin()->first;
		ll cnt = s.rbegin()->second;

		k -= cnt;
		if(k <= 0)
			return{ biggest / 2, (biggest - 1) / 2 };

		s.erase(s.find(biggest));
		s[biggest / 2] += cnt;
		s[(biggest - 1) / 2] += cnt;
	}
	
}

int main() {
#ifdef LOCAL
	// freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cerr << i << endl;
		ll x, k;
		cin >> x >> k;
		pair<ll, ll> ans = brute(x, k);
		cout << "Case #" << i << ": " << ans.first << " " << ans.second << endl;

	}
}