#include <bits/stdc++.h>

using namespace std;

char a[110][110];
int t;

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		int r, c;
		cin >> r >> c;
		cout << "Case #" << tt << ":" << endl;
		for (int i = 1; i <= r; i++)
			for (int j = 1; j <= c; j++)
				cin >> a[i][j];
		for (int i = 1; i <= r; i++)
		{
			for (int j = 1; j < c; j++)
				if (a[i][j] != '?' && a[i][j + 1] == '?')
					a[i][j + 1] = a[i][j];
			for (int j = c; j > 1; j--)
				if (a[i][j] != '?' && a[i][j - 1] == '?')
					a[i][j - 1] = a[i][j];
		}
		for (int i = 1; i < r; i++)
		{
			for (int j = 1; j <= c; j++)
				if (a[i][j] != '?' && a[i + 1][j] == '?')
					a[i + 1][j] = a[i][j];
		}
		for (int i = r; i > 1; i--)
		{
			for (int j = 1; j <= c; j++)
				if (a[i][j] != '?' && a[i - 1][j] == '?')
					a[i - 1][j] = a[i][j];
		}
		for (int i = 1; i <= r; i++)
		{
			for (int j = 1; j <= c; j++)
				cout << a[i][j];
			cout << endl;
		}
	}
	return 0;
}