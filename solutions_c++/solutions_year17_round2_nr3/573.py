#include <bits/stdc++.h>

using namespace std;

#define int int64_t
#define double long double
const int inf = 1e12;

void solve()
{
	int n, q;
	cin >> n >> q;
	int E[n], S[n];
	for(int i = 0; i < n; i++)
		cin >> E[i] >> S[i];
	int D[n][n];
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
		{
			cin >> D[i][j];
			if(D[i][j] == -1)
				D[i][j] = inf;
		}
	for(int k = 0; k < n; k++)
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
	while(q--)
	{
		int st, fi;
		cin >> st >> fi;
		st--, fi--;
		double dist[n];
		fill(dist, dist + n, inf);
		dist[st] = 0;
		set<pair<double, int>> que = {{0, st}};
		while(!que.empty())
		{
			int v = que.begin()->second;
			que.erase(que.begin());
			for(int i = 0; i < n; i++)
				if(D[v][i] <= E[v])
				{
					if(dist[v] + 1. * D[v][i] / S[v] < dist[i])
					{
						que.erase({dist[i], i});
						dist[i] = dist[v] + 1. * D[v][i] / S[v];
						que.insert({dist[i], i});
					}
				}
		}
		cout << dist[fi] << ' ';
	}
	cout << endl;
	
}

signed main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(8);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
