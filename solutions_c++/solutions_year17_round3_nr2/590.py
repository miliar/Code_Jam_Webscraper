#include <bits/stdc++.h>
using namespace std;

int test, n, m;
int a[2][2000];
int l[2000][2000][3][3];

int dp(int x, int y, int u, int v);

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("ou.txt", "w", stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		memset(a, 0, sizeof a);
		memset(l, 255, sizeof l);
		cin >> n >> m;
		for(int i = 0; i < n; i++)
		{
			int x, y;
			cin >> x >> y;
			for(int j = x; j < y; j++)
				a[0][j] = 1;
		}
		for(int i = 0; i < m; i++)
		{
			int x, y;
			cin >> x >> y;
			for(int j = x; j < y; j++)
				a[1][j] = 1;
		}
		int best = 2000;
		if(!a[0][0]) best = min(best, dp(0, 0, 0, 0));
		if(!a[1][0]) best = min(best, dp(0, 0, 1, 1));
		printf("Case #%d: %d\n", t, best);
	}
	return 0;
}

int dp(int x, int y, int u, int v)
{
	if(l[x][y][u][v] >= 0) return l[x][y][u][v];
	if(x == 1440 && y == 720)
	{
		if(u == v) return 0;
		else return 1;
	}
	if(x >= 1440) return 2000;
	int best = 2000;
	if(!a[u][x+1]) best = min(best, dp(x+1, y+u, u, v));
	if(!a[1-u][x+1]) best = min(best, 1 + dp(x+1, y+1-u, 1-u, v));
	l[x][y][u][v] = best;
	return l[x][y][u][v];
}