#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int t;
int tt;
int p;
int n;
int a[4];
int b;
int c;
int g;
int x;

int main()
{
	cin >> t;
	for (tt = 1; tt <= t; ++tt)
	{
		cin >> n >> p;
		a[0] = 0;
		a[1] = 0;
		a[2] = 0;
		a[3] = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> g;
			++a[g%p];
			//cerr << g%p << endl;
		}
		x = a[0];
		//cerr << p << ' ' << a[0] << ' ' << a[1] << endl;
		if (p == 2)
		{
			x += (a[1] + 1) / 2;
		}
		if (p == 3)
		{
			b = max(a[1], a[2]);
			c = min(a[1], a[2]);
			x += c + (b - c + 2) / 3;
		}
		if (p == 4)
		{
			x += a[2] / 2;
			b = max(a[1], a[3]);
			c = min(a[1], a[3]);
			b -= c;
			x += c;
			if (a[2] & 1)
			{
				x += 1 + (b + 1) / 4;
			}
			else
			{
				x += (b + 3) / 4;
			}
		}
		cout << "Case #" << tt << ": " << x << endl;
	}
	return 0;
}
