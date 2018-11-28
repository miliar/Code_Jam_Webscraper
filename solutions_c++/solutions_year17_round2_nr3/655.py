#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int n, q;
long long horsedist[110];
long long horsespeed[110];
long long dist[110][110];
double time[110][110];


void solve(int casen)
{
	for (int i = 0; i < 110; i++)
		for (int j = 0; j < 110; j++)
			time[i][j] = -1;
	scanf("%d %d", &n, &q);
	for (int i = 0; i < n; i++) scanf("%lld %lld", &horsedist[i], &horsespeed[i]);
	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) scanf("%lld", &dist[i][j]);
	for (int i = 0; i < n; i++)dist[i][i] = 0;
	for (int i = 0; i < n; i++)time[i][i] = 0;
	
	//floyd by dist
	for (int k = 0; k < n; k++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (dist[i][k] == -1 || dist[k][j] == -1) continue;
				if (dist[i][j] == -1) dist[i][j] = dist[i][k] + dist[k][j];
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
			}
		}
	}

	//init time dist with given dist pair, horsedist, horsespeed
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (dist[i][j] == -1) continue;
			if (dist[i][j] > horsedist[i]) continue;
			time[i][j] = (double)dist[i][j] / (double)horsespeed[i];
		}
	}

	//floyd by time
	for (int k = 0; k < n; k++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (time[i][k] < -0.5 || time[k][j] < -0.5) continue;
				if (time[i][j] < -0.5) time[i][j] = time[i][k] + time[k][j];
				time[i][j] = min(time[i][j], time[i][k] + time[k][j]);
			}
		}
	}

	
	printf("Case #%d: ", casen);
	//deal with query
	for (int i = 0; i < q; i++)
	{
		int a, b; scanf("%d %d", &a, &b);
		printf("%.9lf ", time[a-1][b-1]);
	}
	puts("");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
}