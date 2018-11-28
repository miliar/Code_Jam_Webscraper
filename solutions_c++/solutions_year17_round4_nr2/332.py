#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int t, tt, n, c, m, x, p, bb, pp, s;
int tic[1001];
int pos[1001];


int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		cin >> n >> c >> m;
		for (int i = 1; i <= n; ++i)
		{
			pos[i] = 0;
		}
		for (int i = 1; i <= c; ++i)
		{
			tic[i] = 0;
		}
		x = 0;
		s = 0;
		p = 0;
		for (int i = 0; i < m; ++i)
		{
			cin >> pp >> bb;
			x = max(x, ++tic[bb]);
			++pos[pp];
		}
		for (int i = 1; i <= n; ++i)
		{
			s += pos[i];
			x = max(x, (s + i - 1) / i);
		}
		for (int i = 1; i <= n; ++i)
		{
			if (pos[i] > x)
			{
				p += pos[i] - x;
			}
		}
		cout << "Case #" << tt << ": " << x << ' ' << p << endl;
	}
	return 0;
}
