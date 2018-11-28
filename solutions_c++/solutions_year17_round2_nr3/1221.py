#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = (sizeof(ll) == 8) ? 1e18 : 1e9;

string ans;

void _case(ll cas)
{
	cout << "Case #" << cas << ": ";
}

void sol(ll cas)
{
	ll n, q, u, v, cur, p;
	cin >> n >> q;
	vector <pair <ll, ll>> arr(n);
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i].first >> arr[i].second;
	}
	vector <ll> d(n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> u;
			if (j == i + 1)
			{
				d[i] = u;
			}
		}
	}
	cin >> u >> v;
	vector <ld> dp(n, (ll)1e15);
	dp[0] = 0;
	ld last;
	for (int i = 0; i < n - 1; i++)
	{
		cur = arr[i].first;
		p = i + 1;
		last = dp[i];
		while ((p < n) && (cur >= d[p - 1]))
		{
			cur -= d[p - 1];
			last += (ld)d[p - 1] / arr[i].second;
			dp[p] = min(dp[p], last);
			p++;
		}
	}
	_case(cas);
	cout << fixed << setprecision(6) << dp.back() << endl;
}

int main()
{
	srand(time(0));
	ios::sync_with_stdio(0);
#ifdef _F1A4X_
	//ifstream cin("input.txt");
	//ofstream cout("output.txt");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ll t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		sol(i + 1);
	}
#ifdef _F1A4X_
	cerr << endl << "\t" << clock() << " ms" << endl;
#endif
}