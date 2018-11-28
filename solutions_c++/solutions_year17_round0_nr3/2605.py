#include <iostream>
#include <sstream>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;


pair < ll, ll > solve(ll n, ll k)
{
	map <ll, ll> mp;
	mp.insert({n, 1});
	while (true)
	{
		auto it = mp.end();
		it--;
		ll cur = it->first;
		ll cnt = it->second;
		mp.erase(cur);
		ll l = cur / 2;
		ll r = (cur - 1) / 2;
		if (k <= cnt)
		{
			return {l, r};
		}
		k -= cnt;
		mp[l] += cnt;
		mp[r] += cnt;
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("a.out", "w+", stdout);
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
		ll n, k;
		cin >> n >> k;
		pair< ll, ll > res = solve(n, k);
		printf("Case #%d: ", t);
		cout << res.first << ' ' << res.second;
		printf("\n");
	}
	return 0;
}