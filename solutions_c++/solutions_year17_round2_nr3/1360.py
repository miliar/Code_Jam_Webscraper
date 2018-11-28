#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main()
{
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small-attempt0.out", "wt", stdout);

	int tests, caseNumber = 0;
	cin >> tests;
	while (++caseNumber <= tests) {
		int n;
		int t;

		
		cin >> n >> t;
		vector < pair<long long, long long> > ds(n);
		vector <long long> d(n);
		for (int i = 0; i < n; ++i)
			cin >> ds[i].first >> ds[i].second;
		d[0] = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j) {
				if (j == i + 1) {
					cin >> d[i + 1];
					d[i + 1] += d[i];
				}
				else {
					cin >> t;
				}
			}
		cin >> t >> t;
		const double inf = -1.0;
		vector<double> ans(n, inf);
		ans[0] = 0.0;
		for (int i = 1; i < n; ++i) {
			for (int j = i - 1; j >= 0; --j) {
				if (d[i] - d[j] <= ds[j].first) {
					if (ans[i] < 0.0) {
						ans[i] = ans[j] + (double)(d[i] - d[j]) / ds[j].second;
					}
					else {
						ans[i] = min(ans[i], ans[j] + (double)(d[i] - d[j]) / ds[j].second);
					}
				}
			}
		}

		
		printf("Case #%d: %.8lf\n", caseNumber, ans[n - 1]);
	}
	return 0;
}
