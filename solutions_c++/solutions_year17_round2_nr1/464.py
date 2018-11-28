#include <bits/stdc++.h>
using namespace std;

double sol()
{
	int k, d, n;
	double last = 0;
	cin >> d >> n;
	for (int i = 1; i <= n; i++)
	{
		int s;
		cin >> k >> s;
		last = max(last, 1. * (d - k) / s);
	}
	return d / last;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
		printf("Case #%d: %.12f\n", i, sol());
	return 0;
}
