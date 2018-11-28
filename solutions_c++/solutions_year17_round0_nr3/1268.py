#include <bits/stdc++.h>
using namespace std;
using uint = unsigned int;
using ll = long long;
using pii = pair<ll, ll>;
#define dbg(x) cerr<<#x": "<<(x)<<'\n'
#define dbg_v(x, n) cerr<<#x"[]: ";for(long long _=0;_<n;++_)cerr<<(x)[_]<<' ';cerr<<'\n'
#define all(v) v.begin(), v.end()

map<ll, ll, greater<ll>> Q;

pii getLens(ll lg)
{
	// 1 2 3 4 5 -> 3
	// 1 2 3 4 -> 2
	ll p = (lg + 1) / 2;
	return {p - 1, lg - p};
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	ll n, k, t, tt, nr;
	pii lens;

	cin >> t;
	for(tt = 1; tt <= t; ++tt)
	{
		cin >> n >> k;
		Q.clear();
		for(Q.insert({n, 1}); ; )
		{
			if((Q.begin()->second) >= k) break;

			lens = getLens(Q.begin()->first);
			nr = Q.begin()->second;
			Q.erase(Q.begin());
			k -= nr;

			Q[lens.first] += nr;
			Q[lens.second] += nr;
			//dbg(lens.first);
			//dbg(lens.second);
		}

		//dbg(Q.begin()->first);

		cout << "Case #" << tt << ": ";

		pii lens = getLens(Q.begin()->first);
		if(lens.first < lens.second) swap(lens.first, lens.second);
		cout << lens.first << ' ' << lens.second << '\n';
	}

	return 0;
}