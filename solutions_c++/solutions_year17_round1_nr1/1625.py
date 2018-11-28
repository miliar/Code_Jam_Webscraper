#include <bits/stdc++.h>
using namespace std;

char s[27][27];
int l[27], r[27], u[27], d[27];

void sol(int cas)
{
	int n, m;
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		cin >> (&(s[i][1]));
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (s[i][j] != '?')
			{
				for (int ii = j - 1; s[i][ii] == '?' && ii > 0; ii--)
					s[i][ii] = s[i][j];
				for (int ii = j + 1; s[i][ii] == '?' && ii <= m; ii++)
					s[i][ii] = s[i][j];
			}
	for (int i = 2; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (s[i][j] == '?')
				s[i][j] = s[i - 1][j];
	for (int i = n - 1; i >= 0; i--)
		for (int j = 1; j <= m; j++)
			if (s[i][j] == '?')
				s[i][j] = s[i + 1][j];
	printf("Case #%d:\n", cas);
	for (int i = 1; i <= n; i++)
		puts(&s[i][1]);
}

int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		sol(i);
	return 0;
}

