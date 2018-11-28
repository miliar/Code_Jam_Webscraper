#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

char c[100][100];
int n, m;
int fr;
int starting[100];

void solve()
{
	scanf("%d %d", &n, &m);
	fr = -1;
	memset(starting, -1, sizeof(starting));
	for (int i = 0; i < n; ++i)
	{
		char ch;
		scanf("%c", &ch);
		for (int j = 0; j < m; ++j)
		{
			scanf("%c", &c[i][j]);
			if (c[i][j] != '?' && fr == -1)
				fr = i;
			if (c[i][j] != '?')
				starting[c[i][j]-'A']=j;
		}
	}
	for (int j = 1; j < m; ++j)
		if (c[fr][j] == '?')
			c[fr][j] = c[fr][j-1];
	for (int j = m-1; j >= 0; --j)
		if (j<m-1 && c[fr][j] == '?')
			c[fr][j] = c[fr][j+1];
	for (int i = fr-1; i >= 0; --i)
		for (int j = 0; j < m; ++j)
			c[i][j] = c[i+1][j];
	for (int i = fr+1; i < n; ++i)
	{
		int code = 1;
		for (int j = 0; j < m; ++j)
			if (c[i][j] == '?')
			{
				if (code == 1)
					c[i][j] = c[i-1][j];
				else
					c[i][j] = c[i][j-1];
			}
			else
			{
				code = 1;
				char cur = c[i-1][j];
				if (starting[cur-'A'] < j)
				{
					for (int k = 0; k < i; ++k)
						for (int l = j; l < m; ++l)
							if (c[k][l] == cur)
								c[k][l] = c[i][j];
				}
				else if (starting[cur-'A'] > j)
				{
					for (int k = 0; k <= i; ++k)
						for (int l = j; l >=0; --l)
							if (c[k][l] == cur)
								c[k][l] = c[i][j];
				}
				else
				{
					code = 0;
					for (int l = 0; l < j; ++l)
						if (c[i][l] == cur)
							c[i][l] = c[i][j];
				}
			}
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
			printf("%c", c[i][j]);
		printf("\n");
	}
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d:\n", i);
		solve();
	}
	return 0;
}