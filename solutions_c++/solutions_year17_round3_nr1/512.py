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


li calc(int idx, int r) {
	if (dp[idx][r] != -1) {
		return dp[idx][r];
	}

	if (r == 1) {
		dp[idx][r] = a[idx].first * a[idx].first + 2 * a[idx].first * a[idx].second;
		if (idx + 1 < n) {
			dp[idx][r] = max(dp[idx][r], calc(idx + 1, r));
		}
		return dp[idx][r];
	}

	dp[idx][r] = -1e16;
	for (int j = idx + 1; j < n; j++) {
		dp[idx][r] = max(dp[idx][r], calc(j, r - 1) - a[j].first * a[j].first);
	}
	return dp[idx][r] = dp[idx][r] + a[idx].first * a[idx].first + 2 * a[idx].first * a[idx].second;
}
li solve2() {

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			dp[i][j] = -1;
		}
	}
	li ans = 0;
	for (int i = 0; i < n; i++) {
		ans = max(ans, calc(i, k));
	}
	return ans;
}
int main() {
#if _DEBUG
#endif

	freopen("A-large (3).in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cout.precision(6);
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cin >> n >> k;
		a = vector<pair<li, li>>(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i].first >> a[i].second;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				dp[i][j] = mxdp[i][j] = 0;
			}
		}
		sort(a.rbegin(), a.rend());

		for (int r = 1; r <= k; r++) {
			for (int idx = n - 1; idx >= 0; idx--) {

				if (r == 1) {
					dp[idx][r] = a[idx].first * a[idx].first + 2 * a[idx].first * a[idx].second;
					if (idx + 1 < n) {
						dp[idx][r] = max(dp[idx][r], dp[idx + 1][r]);
					}
					continue;
				}

				dp[idx][r] = -1e16;


				if (idx + 1 < n)
					dp[idx][r] = max(dp[idx][r], mxdp[idx + 1][r - 1]);
				dp[idx][r] = dp[idx][r] + a[idx].first * a[idx].first + 2 * a[idx].first * a[idx].second;
			}

			for (int idx = n - 1; idx >= 0; idx--) {
				mxdp[idx][r] = dp[idx][r] - a[idx].first * a[idx].first;
				if (idx < n - 1)
					mxdp[idx][r] = max(mxdp[idx][r], mxdp[idx + 1][r]);
			}
		}

		li ans = 0;
		for (int i = 0; i < n; i++) {
			ans = max(ans, dp[i][k]);
		}
		cout << "Case #" << test + 1 << ": " << fixed << ans * PI << endl;
	}
	return 0;
}