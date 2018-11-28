#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

const int maxn = 100+10;
int n, q;
int d[maxn][maxn];
int e[maxn], s[maxn];
double f[maxn];
int vis[maxn];

double dp(int n)
{
	if (vis[n]) return f[n];
	vis[n] = true;
	double &ans = f[n];
	if (n == 0)
		return (ans = 0);
	ans = 1e100;
	double sum = 0;
	for (int i = n-1; i >= 0; --i)
	{
		sum += d[i][i+1];
		if (e[i] < sum)
			continue;
		double cur = (double)sum / s[i];
		double tmp = dp(i);
		if (ans > tmp+cur)
			ans = tmp+cur;
	}
	return ans;
}

void init()
{
	scanf("%d %d", &n, &q);
	for (int i = 0; i < n; ++i)
		scanf("%d %d", &e[i], &s[i]);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			scanf("%d", &d[i][j]);
}

void solve()
{
	while (q-- > 0)
	{
		int u, v;
		scanf("%d %d", &u, &v);
		--u;--v;
		memset(vis, 0, sizeof(vis));
		double ans = dp(n-1);
		printf("%.6lf ", ans);
	}
	printf("\n");
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		init();
		solve();
	}
	return 0;
}