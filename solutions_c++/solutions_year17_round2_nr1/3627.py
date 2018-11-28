#include <bits/stdc++.h>
using namespace std;

pair<double, double> horses [1001];
double d; //destination
int n; //number of horses


int main() {

	freopen("A-Large.in", "rt", stdin);
	freopen("A-Large.out", "wt", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		//take input
		cin >> d >> n;
		for (int i = 0; i < n; i++)
			cin >> horses[i].first >> horses[i].second;

		//sort based on start of each horse
		sort(horses, horses+n);

		double max_time = -1;
		for (int i = n-1; i >= 0; i--) {
			double time = (d - horses[i].first) / horses[i].second;
			max_time = max(max_time, time);
		}

		double ans = d / max_time;
		printf("Case #%d: %.7lf\n", t, ans);
	}
	return 0;
}
