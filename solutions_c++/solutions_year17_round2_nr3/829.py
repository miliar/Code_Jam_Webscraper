#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __ll("$3");

ll n;
ll t;
ll d[101][101];
ll q;
ll e[101];
long double s[101];
vector<pair<long double, ll> > edg[101];
ll bej[101];
ll tal[101];
long double eler[101];
priority_queue<pair<long double, ll> > qq;

long double dijkstra(ll p, ll targ, ll bejid)
{
	if (p==targ) return 0;
	tal[p] = bejid;
	while (!qq.empty()) qq.pop();
	qq.push(make_pair(-0.0, p));
	eler[p] = 0;
	//cerr << "dijkstra " << p << endl;
	while (!qq.empty())
	{
		long double dd = -qq.top().first;
		ll x = qq.top().second;
		//cerr << "tal " << x << ' ' << dd << endl;
		qq.pop();
		if (x == targ) return dd;
		if (bej[x] != bejid)
		{
			bej[x] = bejid;
			for (pair<long double, ll> ed:edg[x])
			{
				if ((tal[ed.second] != bejid) || (eler[ed.second] > dd + ed.first))
				{
					tal[ed.second] = bejid;
					eler[ed.second] = dd + ed.first;
					qq.push(make_pair(-eler[ed.second], ed.second));
				}
			}
		}
	}
	return -2;
}

int main()
{
	cin >> t;
	for (ll tt = 1; tt <= t; ++tt)
	{
		cin >> n >> q;
		for (ll i = 0; i < n; ++i)
		{
			cin >> e[i] >> s[i];
		}
		for (ll i = 0; i < n; ++i)
		{
			for (ll j = 0; j < n; ++j)
			{
				cin >> d[i][j];
			}
		}
		for (ll i = 0; i < n; ++i)
		{
			for (ll j = 0; j < n; ++j)
			{
				for (ll k = 0; k < n; ++k)
				{
					if ((d[i][k] != -1) && (d[k][j] != -1))
					{
						if ((d[i][j] == -1) || (d[i][j] > d[i][k]+d[k][j]))
						{
							d[i][j] = d[i][k] + d[k][j];
						}
					}
				}
			}
		}
		for (ll i = 0; i < n; ++i)
		{
			edg[i].clear();
			for (ll j = 0; j < n; ++j)
			{
				if ((d[i][j] <= e[i]) && (d[i][j] != -1))
				{
					//cerr << "edge " << i << ' ' << j << ' ' << ((long double)d[i][j])/s[i] << endl;
					edg[i].push_back(make_pair(((long double)d[i][j])/s[i], j));
				}
			}
		}
		cout << "Case #" << tt << ":";
		for (ll i = 0; i < q; ++i)
		{
			ll u, v;
			cin >> u >> v;
			--u; --v;
			cout << setprecision(7)<<fixed<<" "<< dijkstra(u, v, 128*tt+i);
		}
		cout << endl;
	}


	return 0;
}
