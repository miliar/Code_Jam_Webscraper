#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <string>

using namespace std;

vector<string> uns = { "R", "O", "Y", "G", "B", "V" };

double calcInter(int x1, int x2, int v1, int v2)
{
	if (x1 == x2) return 0;
	if (v2 <= v1) return INT_MAX;
	return 1.0 * (x1 - x2) / (v2 - v1);
}

typedef long long ll;
const double INF = 1e16;
vector<vector<ll> > d;
vector<pair<ll, ll> > tmp;
vector<pair<ll, ll> > queries;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
#endif

	ll tests, n, q;
	cin >> tests;
	for (ll test = 1; test <= tests; test++) 
	{
		cin >> n >> q;

		tmp.clear();
		tmp.resize(n);
		d.clear();
		d.resize(n, vector<ll>(n));
		queries.clear();
		queries.resize(q);
		vector<ll> x(n);

		for (int i = 0; i < n; i++) 
		{
			cin >> tmp[i].first >> tmp[i].second;
		}

		for (int i = 0; i < n; i++) 
		{
			for (int j = 0; j < n; j++) 
			{
				cin >> d[i][j];
			}
		}

		for (int i = 0; i < q; i++) 
		{
			cin >> queries[i].first >> queries[i].second;
		}

		for (int i = 1; i < n; i++) 
		{
			x[i] = x[i - 1] + d[i - 1][i];
		}

		vector<long double> dp(n, INF);
		dp[0] = 0;
		for (int i = 1; i < n; i++)
		{
			for (int j = 0; j < i; j++) 
			{
				if (x[i] - x[j] <= tmp[j].first)
				{
					dp[i] = min(dp[i], dp[j] + 1.0 * (x[i] - x[j]) / tmp[j].second);
				}
			}
		}

		cout << fixed << setprecision(20);
		cout << "Case #" << test << ": " << dp[n - 1] << endl;
	}
}