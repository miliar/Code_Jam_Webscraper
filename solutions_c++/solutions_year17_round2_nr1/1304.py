#include <bits/stdc++.h>

using namespace std;

double solve()
{
	long long d, n;
	cin >> d >> n;

	double mh = 0;
	for (int i = 0; i < n; i++) {
		long long k, s;
		cin >> k >> s;
		mh = max(mh, (double)(d - k) / s);
	}
	return d / mh;
}

int main()
{
	int t;
	cin >> t;
	cout << fixed << setprecision(6);
	for (int cs = 1; cs <= t; cs++) {
		cout << "Case #" << cs << ": " << solve() << endl;
	}
}
