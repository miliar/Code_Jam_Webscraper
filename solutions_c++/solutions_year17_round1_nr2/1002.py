#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int n, m, cur;
int r[100], a[100][100];
int h[100][100],t[100][100];
int p[100][100];
int point[100];

bool cmp(int a, int b)
{
	if (t[cur][a] != t[cur][b])
		return t[cur][a] < t[cur][b];
	return h[cur][a] < h[cur][b];
}

void solve()
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%d", &r[i]);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			scanf("%d", &a[i][j]);
	int ans = 0;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			h[i][j] = ceil(1/1.1 * a[i][j] / r[i]);
			t[i][j] = floor(1/0.9 * a[i][j] / r[i]);
			//cout << h[i][j] << "," << t[i][j] << " ";
		}
		//cout << endl;
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
			p[i][j] = j;
		cur = i;
		sort(p[i], p[i]+m, cmp);
	}
	for (int i = 0; i < n; ++i)
		point[i] = 0;
	for (int num = 0; num < 10000000; ++num)
	{
		int valid = 1;
		for (int i = 0; i < n; ++i)
		{
			while (point[i]<m && t[i][p[i][point[i]]]<num)++point[i];
			if (point[i] == m)
			{
				printf("%d\n", ans);
				return;
			}
			if (h[i][p[i][point[i]]] > num)
				valid = 0;
		}
		if (valid)
		{
			++ans;
			for (int i = 0; i < n; ++i)
			{
				//cout << " " << point[i];
				++point[i];
			}
			//cout << endl;
			--num;
		}
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}