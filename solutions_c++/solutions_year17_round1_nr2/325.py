#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;



pair<ll ,ll> findCnt(ll have, ll need)
{
	ll mi = need / 100 * 90;
	ll r = have / mi;
	ll mx = need / 100 * 110;
	ll l = (have + mx - 1) / mx;
	return { l, r };
}

int main() {
#ifdef _CONSOLE
	freopen("B-large (3).in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	ll test;
	cin >> test;
	for (ll t = 1; t <= test; ++t)
	{
	
		ll n, p;
		cin >> n >> p;
		vector<ll> v(n);
		for (ll i = 0; i < n; ++i)
		{
			cin >> v[i];
			v[i] *= 100;
		}
		vector<vector<ll> > all(n, vector<ll>(p));
		for (ll i = 0; i < n; ++i)
		{
			for (ll j = 0; j < p; ++j)
			{
				cin >> all[i][j];
				all[i][j] *= 100;
			}
		}
		//unordered_map<ll, unordered_map<ll, ll> > ma;
		map<ll, vector<pair<ll, ll> > > mp;
		for (ll i = 0; i < n; ++i)
		{
			for (ll j = 0; j < p; ++j)
			{
				ll ingr = i;
				pair<ll, ll> cnt = findCnt(all[i][j], v[i]);
				mp[cnt.first].push_back(make_pair(1, i));
				mp[cnt.second + 1].push_back(make_pair(-1, i));
				//ma[cnt][ingr]++;
			}
		}
		vector<ll> cur(n, 0);
		vector<ll> used(n, 0);
		ll ans = 0;
		for (auto it = mp.begin(); it != mp.end(); ++it)
		{
			vector<pair<ll, ll> > &step = it->second;
			for (ll i = 0; i < step.size(); ++i)
			{
				ll num = step[i].second;
				cur[num] += step[i].first;
				if (step[i].first == -1 && used[num] > 0)
				{
					used[num]--;
				}
			}
			ll curans = 1e9;
			for (ll i = 0; i < cur.size(); ++i)
			{
				curans = min(curans, cur[i] - used[i]);
			}
			ans += curans;
			for (ll i = 0; i < cur.size(); ++i)
			{
				used[i] += curans;
			}
		}
		//prllf("Case #%d: %d\n", t, ans);
		cout << "Case #" << t << ": " << ans << "\n";
			
	}

	return 0;
}