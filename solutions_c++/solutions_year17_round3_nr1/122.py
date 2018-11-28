#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <time.h>
#include <algorithm>
#include <list>
#include <math.h>
typedef long long ll;
typedef long double ld;
using namespace std;

const int SZ = 1e3 + 10;
const double INF = 1e18;
const double PI = 3.14159265358979323846;

pair<double, double> x[SZ];
double d[SZ][SZ];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	cout.precision(10);
	
	int t;
	cin >> t;
	for (int testno = 1; testno <= t; testno++) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> x[i].first >> x[i].second;
		x[n].first = x[n].second = 0;
		sort(x, x + n + 1);

		d[0][0] = 0;
		for (int i = 1; i <= k; i++)
			d[0][i] = -INF;

		for (int i = 1; i <= n; i++) {
			d[i][0] = 0;
			for (int j = 1; j <= k; j++) {
				d[i][j] = d[i - 1][j];
				if (d[i - 1][j - 1] != -INF)
					d[i][j] = max(d[i][j], d[i - 1][j - 1] + x[i].second * 2.0 * PI * x[i].first);
			}
		}
		double ans = 0;
		for (int i = 1; i <= n; i++)
			if (d[i][k] != -INF && d[i - 1][k - 1] != -INF)
				ans = max(ans, d[i - 1][k - 1] + x[i].second * 2.0 * PI * x[i].first + PI * x[i].first * x[i].first);

		cout << "Case #" << testno << ": ";
		cout << fixed << ans;
		cout << "\n";
	}

	return 0;
}