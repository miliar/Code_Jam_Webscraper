#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

const int maxn = 1e3 + 5;

pair <long long, long long> pan[maxn];
long double dp[maxn][maxn];

const long double PI = 3.1415926535897932384626433832795;

bool cmp(pair <long long, long long> a, pair <long long, long long> b) {
	return a.first > b.first;
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int q = 0; q < t; q++) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> pan[i].first >> pan[i].second;
		}
		sort(pan, pan + n, cmp);
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= k; j++) {
				dp[i][j] = 0.0;
			}
		}
		for (int i = 0; i < n; i++) {
			dp[i + 1][1] = max(dp[i][1], dp[i][0] + PI * pan[i].first * pan[i].first + 2 * PI * pan[i].first * pan[i].second);
			for (int j = 2; j <= k; j++) {
				dp[i + 1][j] = max(dp[i][j], dp[i][j - 1] + 2 * PI * pan[i].first * pan[i].second);
			}
		}

		cout << "Case #" << q + 1 << ": " << fixed << setprecision(10) << (double)dp[n][k] << '\n';

	}



	return 0;
}