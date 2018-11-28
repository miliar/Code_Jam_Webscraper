#include <bits/stdc++.h>
using namespace::std;

long double dp[1001][1001] = {0.0};

int main() {
	long long t, caseno = 0;
	cin >> t;
	while (t--) {
		for (int i = 0; i <= 1000; i++)
			for (int j = 0; j <= 1000; j++)
				dp[i][j] = 0.0;
		caseno++;
		long long n, k;
		long double ans = 0.0, pie = 3.14159265358979;
		cin >> n >> k;
		vector <pair <long long, long long> > p;
		for (int i = 0; i < n; i++) {
			long long a, b;
			cin >> a >> b;
			p.push_back(make_pair(a, b));
		}
		sort(p.begin(), p.end(), std::greater<pair<long long, long long> >());

		

		dp[0][1] = pie * p[0].first * p[0].first * 1.0 + 2 * pie * p[0].first * p[0].second * 1.0;

		for (long long i = 1; i < n; i++) {
			for (long long j = 1; j <= min(i + 1, k); j++) {
				dp[i][j] = dp[i - 1][j];
				if (j == 1)
					dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] * 1.0 + 2.0 * pie * p[i].first * p[i].second + pie * p[i].first * p[i].first);
				else
					dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] * 1.0 + 2.0 * pie * p[i].first * p[i].second);
			}
		}
		cout << fixed << setprecision(10) << "Case #" << caseno << ": " << dp[n - 1][k] << endl;
	}
	return 0;
}