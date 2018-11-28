#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iterator>
#include <map>
using namespace std;

const int N = 1e3 + 5;
const int K = 26;
typedef long long li;
const li MOD = 1e9 + 7;

li dp[N][N];
li mxdp[N][N];

vector < pair < li, li >> a;
int n, k;
const long double PI = acos(-1.0);

int main() {
#if _DEBUG
	freopen("A-small-attempt1 (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	freopen("C-small-1-attempt1 (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cout.precision(6);
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> p(n);
		for (int i = 0; i < n; i++){
			cin >> p[i];
		}

		double l = 0.0;
		double r = 1.0;

		for (int j = 0; j < 1000; j++) {
			double mid = (l + r) / 2.0;
			double need = 0.0;
			for (int i = 0; i < n; i++) {
				if (p[i] >= mid) continue;
				need += mid - p[i];
			}
			if (need <= u)
				l = mid;
			else
				r = mid;
		}

		double ans = 1.0;

		for (int i = 0; i < n; i++) {
			if (p[i] < l) {
				double can = min(u, l - p[i]);
				p[i] += can;
				u -= can;
			}
			ans *= p[i];
		}
		cout << "Case #" << test + 1 << ": " << fixed << ans << endl;
	}
	return 0;
}