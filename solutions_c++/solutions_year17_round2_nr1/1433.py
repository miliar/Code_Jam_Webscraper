#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int tests, caseNumber = 0;
	cin >> tests;
	while (++caseNumber <= tests) {
		double ans = 0.0;
		int d, n;
		cin >> d >> n;
		vector<pair<int, int>> ks(n);
		for (int i = 0; i < n; ++i) {
			cin >> ks[i].first >> ks[i].second;
		}
		sort(ks.begin(), ks.end());
		vector<double> t(n + 1, 0.0);
		for (int i = n - 1; i >= 0; --i) {
			if (ks[i].first + t[i + 1] * ks[i].second >= d) {
				t[i] = t[i + 1];
			}
			else {
				t[i] = (double)(d - ks[i].first) / ks[i].second;
			}
		}
		ans = d / t[0];
		printf("Case #%d: %.8lf\n", caseNumber, ans);
	}
	return 0;
}

/*
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
*/