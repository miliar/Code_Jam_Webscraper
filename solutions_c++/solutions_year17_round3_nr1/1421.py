#include <iostream>
#include <algorithm>
#include <math.h>

#define pi acos(-1.0)

using namespace std;

struct list {
	int r, h;
	double s;
	bool operator()(list i, list j) {
		return i.r > j.r;
	}
	void make() {
		double x = r, y = h;
		s = 2.0 * pi *x * y;
	}
	double nb() {
		return pi*r*r;
	}
}d[10005];

double dp[1005][1005];

int main() {
	freopen("text.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		double ans = 0;
		int n, m; cin >> n >> m;

		for (int i = 0; i < n; i++) {
			cin >> d[i].r >> d[i].h;
			d[i].make();
		}

		sort(d, d + n, list());

		for (int i = 0; i < n; i++) {
			dp[0][i] = d[i].nb() + d[i].s;
			ans = max(ans, dp[0][i]);
		}

		for (int i = 1; i < m; i++) {
			double mx = 0;
			for (int j = i; j < n; j++) {
				mx = max(mx, dp[i - 1][j - 1]);
				dp[i][j] = max(dp[i][j - 1], mx + d[j].s);
				ans = max(ans, dp[i][j]);
			}
		}

		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++) dp[i][j] = 0;


		printf("Case #%d: %.9lf\n", tc, ans);	}
}