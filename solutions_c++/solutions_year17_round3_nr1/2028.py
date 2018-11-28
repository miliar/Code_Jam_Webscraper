#include <bits/stdc++.h>

using namespace std;

#define ABS(x) ((x) < 0 ? -(x) : (x))
#define ld long double
#define ll long long
#define uint unsigned int
#define all(a) a.begin(), a.end()
#ifdef DEBUG
    #define NAME "1"
#else
    #define NAME "fox-blocks"
#endif
#define FREOPEN freopen(NAME".in", "r", stdin); freopen(NAME".out", "w", stdout)
#define PI 3.1415926535897932384626433832795

const double EPS = 1e-9;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	cout << fixed << setprecision(7);
	for (int qq = 1; qq <= t; ++qq) {
		cout << "Case #" << qq << ": ";
		int n, k;
		cin >> n >> k;
		vector<pair<ld, ld>> mas(n);
		for (int i = 0; i < n; ++i) {
			cin >> mas[i].first >> mas[i].second;
		}
		sort(all(mas));
		ld ans = 0.0;
		ld dp[n + 1][k + 1], mx[k + 1][n + 1];
		for (int i = 0; i <= n; ++i)
			for (int j = 0; j <= k; ++j) {
				dp[i][j] = 0.0;
				mx[j][i] = 0.0;
			}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= k; ++j) {
				for (int prev = i - 1; prev >= 0; --prev) {
					ld now = 0.0;
					if (prev > 0)
						now = PI * mas[prev - 1].first * mas[prev - 1].first;
					dp[i][j] = max(dp[i][j], dp[prev][j - 1] + 2 * PI * mas[i - 1].first * mas[i - 1].second + PI * mas[i - 1].first * mas[i - 1].first - now);
					ans = max(ans, dp[i][j]);
				}
			}
		}
		cout << ans << "\n";
	}
	return 0;
}