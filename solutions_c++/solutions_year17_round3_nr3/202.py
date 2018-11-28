#include <bits/stdc++.h>

using namespace std;
typedef long double ll;
#define BR __int("$3");

int t;
int tt;
int n;
int k;
ll u;
ll p[51];
int x;
ll r;
ll s;

int main()
{
	cin >> t;
	for (tt = 1; tt <= t; ++tt)
	{
		cin >> n >> k;
		cin >> u;
		for (int i = 0; i < n; ++i)
		{
			cin >> p[i];
		}
		sort(p, p + n);
		x = 1;
		s = p[0];
		for (int i = 1; i < n; ++i)
		{
			if ((p[i] - s) * x <= u)
			{
				u -= (p[i] - s) * x;
				++x;
				s = p[i];
			}
			else
			{
				s += u / x;
				u = 0;
				break;
			}
		}
		if (u > 0)
		{
			s += u / x;
			++x;
		}
		for (int i = 0; i < x; ++i)
		{
			p[i] = s;
		}
		r = 1.0;
		for (int i = 0; i < n; ++i)
		{
			r *= p[i];
		}
		cout << setprecision(7);
		cout << "Case #" << tt << ": " << r << endl;
	}


	return 0;
}
