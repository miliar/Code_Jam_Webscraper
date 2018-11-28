#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long a[105][105];
double t[105][105];
long long e[105], s[105];

void solve()
{
	int n, q;
	scanf("%d%d", &n, &q);
	for (int i = 0; i < n; ++i)
	{
		scanf("%lld%lld", &e[i], &s[i]);
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			scanf("%lld", &a[i][j]);
		}
	}
	for (int i = 0; i < n; ++i)
	{
		a[i][i] = 0;
	}
	for (int k = 0; k < n; ++k)
	{
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (a[i][k] != -1 && a[k][j] != -1)
				{
					long long nd = a[i][k] + a[k][j];
					a[i][j] = a[i][j] == -1 ? nd : min(a[i][j], nd);
				}
			}
		}
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			t[i][j] = a[i][j] != -1 && e[i] >= a[i][j] ? ((double)a[i][j])/s[i] : -1;
		}
	}
	for (int k = 0; k < n; ++k)
	{
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (t[i][k] != -1 && t[k][j] != -1)
				{
					double nd = t[i][k] + t[k][j];
					t[i][j] = t[i][j] == -1 ? nd : min(t[i][j], nd);
				}
			}
		}
	}
	for (int i = 0; i < q; ++i)
	{
		int u, v;
		scanf("%d%d", &u, &v);
		printf("%.8lf ", t[u - 1][v - 1]);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
