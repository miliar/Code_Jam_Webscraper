#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		long double d;
		int n;
		cin >> d >> n;
		long double u = -1;
		for (int i = 0; i < n; ++i)
		{
			long double k;
			long double s;
			long double v;
			cin >> k >> s;
			v = (d-k) / s;
			if (u < v)
				u = v;
		}
		cout << setprecision(7) << fixed << "Case #" << tt << ": " << d/u << endl;
	}
	return 0;
}
