#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;
int a[100], p[100];
int q[100][100], l[100][100], r[100][100];

void Solve()
{
	int n, m;
	scanf("%d %d\n", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			scanf("%d", &q[i][j]);
		sort(&q[i][0], &q[i][0] + m);
		for (int j = 0; j < m; j++)
		{
			r[i][j] = (q[i][j] * 10) / (a[i] * 9);
			l[i][j] = (q[i][j] * 10 - 1) / (a[i] * 11) + 1;
		}
		p[i] = m - 1;
	}
	int ans = 0;
	while (true)
	{
		int minr = 10000001, maxl = -1, index = -1;
		for (int i = 0; i < n; i++)
		{
			if (l[i][p[i]] > maxl)
			{
				maxl = l[i][p[i]];
				index = i;
			}
			if (r[i][p[i]] < minr)
				minr = r[i][p[i]];
		}
		if (maxl <= minr)
		{
			ans++;
			for (int i = 0; i < n; i++)
				p[i]--;
		}
		else
		{
			p[index]--;
		}
		bool flag = false;
		for (int i = 0; i < n; i++)
			flag = (p[i] == -1);
		if (flag) break;
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}