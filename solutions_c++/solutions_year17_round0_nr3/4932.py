#include <bits/stdc++.h>
#define ll long long
using namespace std;

typedef map<pair<ll, ll>, ll> Map;

bool bi[1000002];
Map M[1000002];

map<ll, bool>u;
map<ll, Map>Ans;

Map& preprocess(int i, int j)
{
	int d = j - i;
	if(bi[d])
	{
		return M[d];
	}
	bi[d] = true;
	M[d].clear();
	if(!d)
	{
		M[d][make_pair(0, 0)] = 1;
		return M[d]; 
	}

	int mid = (i + j) >> 1;
	if(i <= mid - 1)
	{
		Map &k = preprocess(i, mid - 1);
		Map::iterator it = k.begin();

		for(; it != k.end(); it++)
		{
			M[d][it->first] = M[d][it->first] + it->second;
		}
	}
	if(mid + 1 <= j)
	{
		Map &k = preprocess(mid + 1, j);
		Map::iterator it = k.begin();

		for(; it != k.end(); it++)
		{
			M[d][it->first] = M[d][it->first] + it->second;
		}
	}
	M[d][make_pair(min(mid - i, j - mid), max(mid - i, j - mid))]++;

	return M[d];
}

Map& process(ll i, ll j)
{
	ll d = j - i;
	if(d <= 10000ll)
	{
		return M[d];
	}
	if(u[d])
	{
		return Ans[d];
	}
	u[d] = true;
	Ans[d].clear();

	ll mid = (i + j) / 2;
	if(i <= mid - 1)
	{
		Map &k = process(i, mid - 1);
		Map::iterator it = k.begin();

		for(; it != k.end(); it++)
		{
			Ans[d][it->first] = Ans[d][it->first] + it->second;
		}
	}
	if(mid + 1 <= j)
	{
		Map &k = process(mid + 1, j);
		Map::iterator it = k.begin();

		for(; it != k.end(); it++)
		{
			Ans[d][it->first] = Ans[d][it->first] + it->second;
		}
	}
	Ans[d][make_pair(min(mid - i, j - mid), max(mid - i, j - mid))]++;

	return Ans[d];
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	Map m;

	for(int i = 1; i <= 100000; i++)
	{
		m = preprocess(1, i);
	}

	/*u.clear();
	Ans.clear();

	m = process(1, 1000000);

	for(; it != m.end(); it++)
	{
		printf("(%lld, %lld) %lld\n", it->first.first, it->first.second, it->second);
	}*/

	int tc;
	scanf("%d", &tc);

	Map::iterator it;

	for(int t = 1; t <= tc; t++)
	{
		printf("Case #%d: ", t);
		ll n, k;

		cin>>n>>k;

		ll cnt = 0;

		u.clear();
		Ans.clear();

		Map m = process(1ll, n);

		it = m.end();
		it--;

		for(; ; it--)
		{
			k = k - it->second;
			if(k <= 0)
			{
				printf("%lld %lld\n", it->first.second, it->first.first);
				break;
			}
		}
	}

	return 0;
}