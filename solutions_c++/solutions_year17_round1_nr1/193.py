#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;
char c[100][100];

void Solve()
{
	int n, m;
	scanf("%d %d\n", &n, &m);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			scanf("%c", &c[i][j]);
		scanf("\n");
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j < m; j++)
			if (c[i][j - 1] != '?' && c[i][j] == '?')
				c[i][j] = c[i][j - 1];
		for (int j = m-2; j >=0; j--)
			if (c[i][j + 1] != '?' && c[i][j] == '?')
				c[i][j] = c[i][j + 1];
	}

	for (int i = 0; i < m; i++)
	{
		for (int j = 1; j < n; j++)
			if (c[j - 1][i] != '?' && c[j][i] == '?')
				c[j][i] = c[j - 1][i];
		for (int j = n - 2; j >= 0; j--)
			if (c[j + 1][i] != '?' && c[j][i] == '?')
				c[j][i] = c[j + 1][i];
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			printf("%c", c[i][j]);
		printf("\n");
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: \n", i + 1);
		Solve();
	}
}