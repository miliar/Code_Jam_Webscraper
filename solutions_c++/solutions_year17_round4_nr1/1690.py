#include <bits/stdc++.h>

using namespace std;

int T, n;
int g[120];
int p;
int c[5];

int main()
{
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		for (int i = 0; i < 5; i++) c[i] = 0;
		cin >> n >> p;
		for (int i = 0; i < n; i++)
		{
			cin >> g[i];
			g[i] %= p;
			c[g[i]]++;
		}
		int ans;
		if (p == 2)
		{
			ans = n - c[1]/2;
		}
		else if (p == 3)
		{
			ans = n;
			ans -= min(c[1], c[2]);
			int d = max(c[1], c[2]) - min(c[1], c[2]);
			ans -= 2*d/3;
		}
		cout << "Case #" << C << ": " << ans << '\n';
	}
	return 0;
}
