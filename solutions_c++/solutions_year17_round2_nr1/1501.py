#include <bits/stdc++.h>

using namespace std;

int t;

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		long double ans = 1000ll * 1000ll * 10000ll, d;
		ans = ans * ans + 100;
		int n;
		cin >> d >> n;
		for (int i = 0; i < n; i++)
		{
			long double p, v;
			cin >> p >> v;
			ans = min(ans, (d * v) / (d - p));
		}
		cout << setprecision(8) << fixed << ans << endl;
	}
	return 0;
}