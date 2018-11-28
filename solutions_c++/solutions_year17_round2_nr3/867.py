#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <set>

#define sz(x) ((int64)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

void solve() {
    int64 n;
	cin >> n;
	int64 q;
	cin >> q;
	vector<int64> e(n), s(n);
	for (int64 i = 0; i < n; ++i) {
		cin >> e[i] >> s[i];
	}
	vector<vector<int64>> d(n, vector<int64>(n));
	for (int64 i = 0; i < n; ++i) {
		for (int64 j = 0; j < n; ++j) {
			cin >> d[i][j];
		}
	}
	vector<int64> distance(n, 0);
	for (int64 i = 1; i < n; ++i) {
		distance[i] = distance[i - 1] + d[i - 1][i];
	}
	vector<double> dp(n, 1e100);
	dp[0] = 0;
	for (int64 i = 1; i < n; ++i) {
		for (int64 j = 0; j < i; ++j) {
			int64 local_distance = distance[i] - distance[j];
			if (local_distance > e[j]) {
				continue;
			}
			dp[i] = min(dp[i], dp[j] + 1.0 * local_distance / s[j]);
		}
	}
	int64 v, u;
	cin >> v >> u;
	cout.precision(12);
	cout << dp[n - 1] << endl;
}

int main() {
    int64 tests;
    cin >> tests;
    for (int64 test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
