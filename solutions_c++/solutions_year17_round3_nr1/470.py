#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

#define SZ(a) (int)(a).size()
typedef long long ll;

const long double pi = abs(atan2(0.l, -1.l));

int itc;

void solve() {
	int n, k;
	cin >> n >> k;
	vector<pair<int, int>> a;
	for (int i = 0; i < n; i++) {
		int r, h;
		cin >> r >> h;
		a.push_back({r, h});
	}
	sort(begin(a), end(a), greater<pair<int, int>>());
	vector<ll> dp(k+1, 0);
	for (int i = 0; i < n; i++) {
		int r = a[i].first;
		int h = a[i].second;
		for (int j = min(i, k-1); j >= 1; j--) {
			dp[j+1] = max(dp[j+1], dp[j] + 2ll*r*h);
		}
		dp[1] = max(dp[1], r*(r+2ll*h));
	}
	printf("%.9Lf\n", dp[k]*pi);
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
