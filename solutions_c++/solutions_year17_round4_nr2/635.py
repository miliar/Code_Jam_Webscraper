#include <bits/stdc++.h>
using namespace std;

#pragma GCC diagnostic warning "-Wconversion"

#define pb push_back
#define mp make_pair
#define eb emplace_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)
#define maxval(t) numeric_limits<t>::max()
#define minval(t) numeric_limits<t>::min()
#define imin(a, b) a = min(a, b)
#define imax(a, b) a = max(a, b)

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

using ll = long long;

ll n;
ll need[2000];
ll rides[2000];

ll check(ll res)
{
	ll spare = 0;
	ll pro = 0;

	fora(i, n)
	{
		spare += res - need[i];
		if (spare < 0)
			return -1;
		pro += max(0LL, need[i] - res);
	}
	return pro;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	forb(t, T)
	{
		ll res = 0;

		ll c, m;
		cin >> n >> c >> m;

		fill(all(rides), 0);
		fill(all(need), 0);

		fora(i, m)
		{
			int b, p;
			cin >> p >> b;
			rides[b - 1]++;
			need[p - 1]++;
		}

		ll mostr = minval(ll);
		fora(i, c)
		{
			imax(mostr, rides[i]);
		}

		for (ll i = mostr; i < 1001; i++)
		{
			ll poss = check(i);
			if (poss >= 0)
			{
				cout << "Case #" << t << ": " << i << " " << poss << endl;
				break;
			}
		}

	}
}
