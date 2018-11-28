#include <bits/stdc++.h>

using namespace std;

void solve()
{
	int d, n;
	cin >> d >> n;
	double ans = 0;
	for(int i = 0; i < n; i++)
	{
		int k, s;
		cin >> k >> s;
		ans = max(ans, 1. * (d - k) / s);
	}
	cout << fixed << setprecision(8) << d / ans << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
