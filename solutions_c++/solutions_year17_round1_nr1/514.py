#include <bits/stdc++.h>

using namespace std;

const int maxn = 26;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int n, m;
		string s[maxn];
		printf("Case #%d:\n", t);
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
		{
			cin >> s[i];
			char last = '?';
			for (int j = 0; j < m; ++j)
			{
				if (s[i][j] != '?')
					last = s[i][j];
				else
					s[i][j] = last;
			}
			for (int j = m - 1; j >= 0; --j)
			{
				if (s[i][j] != '?')
					last = s[i][j];
				else
					s[i][j] = last;
			}
		}
		for (int j = 0; j < m; ++j)
		{
			char last = '?';
			for (int i = 0; i < n; ++i)
			{
				if (s[i][j] != '?')
					last = s[i][j];
				else
					s[i][j] = last;
			}
			for (int i = n - 1; i >= 0; --i)
			{
				if (s[i][j] != '?')
					last = s[i][j];
				else
					s[i][j] = last;
			}
		}
		for (int i = 0; i < n; ++i)
			cout << s[i] << endl;
	}
}
 
