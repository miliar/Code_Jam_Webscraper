#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;

int f[101][101][101][101][4];
int a[4];
int ans;

void Solve()
{
	int n, p;
	scanf("%d %d", &n, &p);
	memset(a, 0, sizeof(a));
	for (int i = 0; i < n; i++)
	{
		int x;
		scanf("%d", &x);
		a[x % p]++;
	}
	for (int ii = 0; ii <= a[0]; ii++)
		for (int i = 0; i <= a[1]; i++)
			for (int j = 0; j <= a[2]; j++)
				for (int k = 0; k <= a[3]; k++)
					for (int l = 0; l < p; l++)
						f[ii][i][j][k][l] = -n;
	f[0][0][0][0][0] = 0;
	int ans = 0;
	for (int ii = 0; ii <= a[0]; ii++)
		for (int i = 0; i <= a[1]; i++)
			for (int j = 0; j <= a[2]; j++)
				for (int k = 0; k <= a[3]; k++)
					for (int l = 0; l < p; l++)
					{
						if (ii > 0)
							f[ii][i][j][k][l] = max(f[ii][i][j][k][l], f[ii - 1][i][j][k][l] + (l == 0));
						if (i > 0)
							f[ii][i][j][k][l] = max(f[ii][i][j][k][l], f[ii][i - 1][j][k][(l - 1 + p + p) % p] + ((l - 1 + p + p) % p == 0));
						if (j > 0)
							f[ii][i][j][k][l] = max(f[ii][i][j][k][l], f[ii][i][j - 1][k][(l - 2 + p + p) % p] + ((l - 2 + p + p) % p == 0));
						if (k > 0)
							f[ii][i][j][k][l] = max(f[ii][i][j][k][l], f[ii][i][j][k - 1][(l - 3 + p + p) % p] + ((l - 3 + p + p) % p == 0));
						ans = max(ans, f[ii][i][j][k][l]);
					}
	printf("%d\n", ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}
