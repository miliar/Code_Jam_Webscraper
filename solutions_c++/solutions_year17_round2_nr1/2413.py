#include <bits/stdc++.h>

using namespace std;

double solve()
{
	double d;
	int n;
	cin >> d >> n;
	double time = 0;
	for (int i = 0; i < n; i++)
	{
		double k, s;
		cin >> k >> s;
		time = max(time, (d - k) / s);
	}
	return d / time;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		double ans = solve();
		printf("Case #%d: %.9f\n", i + 1, ans);
	}
	return 0;
}
