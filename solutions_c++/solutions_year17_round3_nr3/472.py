#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long lint;
typedef double db;
const int N = 55;
double dp[N][N];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n, k;
		double up;
		vector < double > v;
		scanf("%d%d", &n, &k);
		scanf("%lf", &up);
		for (int i = 0; i < n; ++i) {
			double x;
			scanf("%lf", &x);
			v.push_back(x);
		}
		double l = 0, r = 1.0;
		for (int t = 0; t < 200; ++t) {
			double m = (l + r) / 2;
			double cost = 0.0;
			for (int i = 0; i < n; ++i) {
				if (v[i] <= m)
					cost += (m - v[i]);
			}
			if (cost < up) {
				l = m;
			}
			else {
				r = m;
			}
		}
		double ans = 1.0;
		for (int i = 0; i < n; ++i) {
			if (v[i] < l)
				ans *= l;
			else
				ans *= v[i];
		}
		printf("Case #%d: %.8lf\n", i, ans);
	}
	return 0;
}