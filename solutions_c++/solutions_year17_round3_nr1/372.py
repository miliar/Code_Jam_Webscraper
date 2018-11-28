#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstdio>

using namespace std;

#define PI acos(-1)

typedef pair<long long int, long long int> P;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, k;
		cin >> n >> k;
		long long int r, h;
		vector<P> pan;
		for (int j = 0; j < n; j++) {
			cin >> r >> h;
				pan.push_back(P(r, h));
		}
		sort(pan.begin(), pan.end(), greater<P>());
		/*for (int j = 0; j < pan.size(); j++) {
			cout << pan[j].first << ' ' << pan[j].second << endl;
		}*/
		vector< vector<long long int> > dp(n + 1, vector<long long int>(k+1, 0));
		for (int j = 0; j < n; j++) {
			long long int mm = 2 * pan[j].first*pan[j].second;
			long long int MM = pan[j].first*pan[j].first + mm;
			dp[j + 1][1] = max(MM, dp[j][1]);
			for (int kk = 2; kk <= min(k, j+1); kk++) {
				dp[j + 1][kk] = max(dp[j][kk], dp[j][kk - 1] + mm);
			}
			//cout << MM << endl;
		}/*
		for (int j = 0; j <= n; j++) {
			for (int kk = 0; kk <= k; kk++) {
				cout << dp[j][kk] << ' ';
			}
			cout << endl;
		}
		cout << dp[n][k] << endl;*/
		double ans = (double)dp[n][k] * PI;
		printf("Case #%d: %.9f\n", i+1, ans);
	}
	return 0;
}