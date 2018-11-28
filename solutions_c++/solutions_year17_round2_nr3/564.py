/*
Hanit Banga
*/

#include <algorithm>
#include "iomanip"
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false)

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int N = 110;
const double inf = 1e18;

double d[N][N], dist[N][N], e[N], s[N], dp[N][N][N];

void floyd_warshall(int n);

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		int n, q;
		cin >> n >> q;
		for (int i = 1; i <= n; ++i)
			cin >> e[i] >> s[i];

		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				cin >> d[i][j];

		floyd_warshall(n);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				d[i][j] = ((dist[i][j] <= e[i]) ? (dist[i][j] / s[i]) : -1);

		floyd_warshall(n);
		while (q--)
		{
			int u, v;
			cin >> u >> v;
			cout << fixed << setprecision(7) << dist[u][v] << ' ';
		}

		cout << endl;
	}	
}

void floyd_warshall(int n)
{
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			dp[i][j][0] = ((d[i][j] < 0) ? inf : d[i][j]);

	for (int i = 1; i <= n; ++i)
		dp[i][i][0] = 0;

	for (int k = 1; k <= n; ++k)
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				dp[i][j][k] = min(dp[i][j][k - 1], dp[i][k][k - 1] + dp[k][j][k - 1]);

	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			dist[i][j] = dp[i][j][n];
}