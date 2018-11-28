#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
using ll = long long;
#define EPS 0.000000001
#define NMAX 60

long double p[NMAX];

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	#endif

	int t, tt, i, j, n, k;
	long double ans, u, add;

	cin >> t;
	for(tt = 1; tt <= t; ++tt)
	{
		cin >> n >> k >> u;
		for(i = 0; i < n; ++i) cin >> p[i];

		sort(p, p + n);

		for(i = 0; i < n && u > EPS; i = j)
		{
			for(j = i; j < n && abs(p[i] - p[j]) < EPS; ++j);

			add = u / j;
			if(j < n) add = min(add, p[j] - p[j - 1]);

			for(k = 0; k < j; ++k) p[k] += add;
			u -= add * j;
			//cerr << add << ' ' << u << '\n';
		}

		for(ans = 1.0, i = 0; i < n; ++i) ans *= p[i];

		cout << "Case #" << tt << ": " << ans << '\n';
	}

	return 0;
}