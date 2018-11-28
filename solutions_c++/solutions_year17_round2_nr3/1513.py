#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, ignore;
	cin >> n >> ignore;
	vector<pair<int, int>> horses(n);
	for(auto &h : horses) {
		cin >> h.first >> h.second;
	}
	vector<int> dist(n - 1);
	for(int i = 1; i < n; ++i) {
		for(int j = 0; j < i; ++j) {
			cin >> ignore;
		}
		cin >> dist[i - 1];
		for(int j = 1; j < n - i; ++j) {
			cin >> ignore;
		}
	}
	for(int i = 0; i < n + 2; ++i) {
		cin >> ignore;
	}
	vector<double> dp(n, numeric_limits<double>::max());
	dp[0] = 0;
	for(int i = 1; i < n; ++i) {
		long long d = 0;
		for(int j = i - 1; j >= 0; --j) {
			if((d += dist[j]) <= horses[j].first) {
				dp[i] = min(dp[i], dp[j] + double(d) / horses[j].second);
			}
		}
	}
	cout << ' ' << setprecision(7) << dp[n - 1] << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
