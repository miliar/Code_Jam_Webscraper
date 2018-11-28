#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;
int n, m, c;
int a[2000][2], s[2], z[2];

int edge[2000][2000];
int match[2000];
int check[2000];
bool find(int u)
{
	for (int i = 0; i < m; i++)
	{
		if (edge[u][i] && !check[i])
		{
			check[i] = 1;
			if (match[i] == -1 || find(match[i]))
			{
				match[i] = u;
				return true;
			}
		}
	}
	return false;
}

void Solve()
{
	memset(a, 0, sizeof(a));
	memset(s, 0, sizeof(s));
	memset(z, 0, sizeof(z));
	scanf("%d %d %d", &n, &c, &m);
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &a[i][0], &a[i][1]);
		a[i][0]--;
		a[i][1]--;
		if (a[i][0] == 0)
			z[a[i][1]]++;
		s[a[i][1]]++;
	}
	int ans = z[0] + z[1] + max(max(0, (s[0] - z[1] - z[0])), max(0, (s[1] - z[1] - z[0])));

	printf("%d ", ans);
	memset(edge, 0, sizeof(edge));

	for (int i = 0; i < m; i++)
		for (int j = 0; j < m; j++)
			if (a[i][0] != a[j][0] && a[i][1] == 0 && a[j][1] == 1)
			{
				edge[i][j] = true;
			}
	memset(match, 255, sizeof(match));
	int tot = 0;
	for (int i = 0; i < m; i++)
	{
		memset(check, 0, sizeof(check));
		if (find(i))
			tot++;
	}
		
	printf("%d\n", s[0] + s[1] - tot - ans);
}

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}
