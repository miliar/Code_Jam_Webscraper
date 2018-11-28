#include <bits/stdc++.h>

using namespace std;

int test, n, p;
int g[111];
int c[111][111][111];
int b[5];

int check(int i, int j, int k)
{
	return ((i+j*2+k*3)%p) == 0;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> test;
	
	for(int t = 1; t <= test; t++)
	{
		cin >> n >> p;
		for(int i = 0; i < n; i++)
			cin >> g[i];
		memset(b, 0, sizeof b);
		for(int i = 0; i < n; i++)
			b[g[i]%p]++;
		c[0][0][0] = 0;
		for(int i = 0; i <= b[1]; i++)
			for(int j = 0; j <= b[2]; j++)
				for(int k = 0; k <= b[3]; k++)
				if(!(i+j+k == 0))
				{
					c[i][j][k] = 0;
					if(i > 0)
						c[i][j][k] = max(c[i][j][k], c[i-1][j][k] + check(i-1, j, k));
					if(j > 0)
						c[i][j][k] = max(c[i][j][k], c[i][j-1][k] + check(i, j-1, k));
					if(k > 0)
						c[i][j][k] = max(c[i][j][k], c[i][j][k-1] + check(i, j, k-1));
				}
		int rs = b[0] + c[b[1]][b[2]][b[3]];
		printf("Case #%d: %d\n", t, rs);
	}
	return 0;
}

