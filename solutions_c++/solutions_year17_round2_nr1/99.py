#include <bits/stdc++.h>

#define ff first
#define ss second
#define pii pair < int, int >
#define puba push_back

using namespace std;

typedef long long LL;

const int MAXN = 1010;

double poses[MAXN], speed[MAXN];


const double INF = 1e18;
const double EPS = 1e-10;
const int ITER = 200;

int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";
		int n;
		double d;
		cin >> d >> n;

		for (int i = 0; i < n; ++i) {
			cin >> poses[i] >> speed[i];
		}

		double ans = INF;

		for (int i = 0; i < n; ++i) {
			ans = min(ans, d * speed[i] / (d - poses[i]));
		}

		printf("%.13lf\n", ans);
	}
	return 0;
}