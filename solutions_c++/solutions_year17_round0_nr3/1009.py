/*
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▐▐▐▐▐▐░░░░░░░
░░░░░░░░░░▐▐▌▌▌▌▌▌▐▐░░░░░
░░░░░░░░░▐▌▌▌▌▌▌▌▌▌▌▐░░░░
░░░░░░░░▐░░▌◐░▌▌▌◐░░░▐░░░
░░░░░░░░▐░░░░░░░░░░░░▐░░░  
░░░░░░░░▐░░░░░▐░░░░░░▐░░░
░░░░░░░░░▐░░░▐▐▐░░░░░▐░░░
░░░░░░░░░▐░░░░░░░░░░▐░░░░
░░░░░░░░░░▐░░████░░▐░░░░░
запускаем░░▐░░░░░░░▐░░░░░
░░░░Влада░░▐░░░░░░▐░░░░░░
░░░Макеева░░▐░░░░▐░░░░░░░
░░░░░░░░░░░░░▐▐▐▐░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define zhfs main
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second
#define re return
#define forn(i, n) for (int i = 1; i <= n; i++)
map<ll, map<ll, ll> > dp;
map<ll, ll> calc(ll x)
{
	if (dp.count(x)) return dp[x];
	if (x == 0) return map<ll, ll>();
	map<ll, ll> res;
	res[x] = 1;
	ll mid = x / 2;
	map<ll, ll> gol = calc(mid), gor = calc(x - 1 - mid);
	for (auto v : gol)
	{
		res[v.first] += v.second;
	}
	for (auto v : gor)
	{
		res[v.first] += v.second;
	}
	dp[x] = res;
	return res;
}
int zhfs()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		ll n, k;
		scanf("%lld %lld", &n, &k);
		map<ll, ll> tmp = calc(n);
		vector<pair<ll, ll> > go;
		for (auto v : tmp) go.push_back(v);
		sort(go.rbegin(), go.rend());
		ll goLen = -1;
		for (int i = 0; i < (int)go.size(); i++)
		{
			if (go[i].second >= k)
			{
				goLen = go[i].first;
				break;
			}
			else
			{
				k -= go[i].second;
			}
		}
		printf("Case #%d: %lld %lld\n", tt,  goLen / 2, goLen - 1 - goLen / 2);
	}
}

