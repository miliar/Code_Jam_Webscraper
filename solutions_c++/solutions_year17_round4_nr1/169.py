#include <iostream>
#include <bits/stdc++.h>


using namespace std;

#define re return
#define mp make_pair
#define forn(i, n) for (int i = 0; i < n; i++)
#define sz(a) int(a.size())
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int t, n, p, dp[101][101], dp1[101][101][101];
vector<int> k;

void solve() {
	cin >> n >> p;
	k.assign(p, 0);
	forn (i, n) {
		int c;
		cin >> c;
		k[c % p]++;
	}
	int ans = k[0];
	k[0] = 0;
	if (p == 2) {
		ans += k[1] / 2 + k[1] % 2;
	} 
	if (p == 3) {
		ans += dp[k[1]][k[2]];
	}
	if (p == 4) {
		ans += dp1[k[1]][k[2]][k[3]];
	}
	cout << ans << "\n";
}
int main() {
	iostream::sync_with_stdio(0), cin.tie(0);
	freopen("a.out", "w", stdout);
	cin >> t;
	dp[0][0] = 0;
	for (int i = 0; i <= 100; i++) {
		for (int j = 0; j <= 100; j++) {
			if (i || j) dp[i][j] = 1;
			if (i && j)
				dp[i][j] = max(dp[i][j], dp[i  -1][j - 1] + 1);
			if (i >= 3)
				dp[i][j] = max(dp[i][j], dp[i - 3][j] + 1);
			if (j >= 3)
				dp[i][j] = max(dp[i][j], dp[i][j - 3] + 1);
		}
	}
	for (int i = 0; i <= 100; i++) {
		for (int j = 0; i + j <= 100; j++) {
			for (int k = 0; i + j + k <= 100; k++) {
				if (i || j || k)
					dp1[i][j][k] = 1;
				if (i >= 4)
					dp1[i][j][k] = max(dp1[i][j][k], dp1[i - 4][j][k] + 1);
				if (k >= 4)
					dp1[i][j][k] = max(dp1[i][j][k], dp1[i][j][k - 4] + 1);
				if (i && k)
					dp1[i][j][k] = max(dp1[i][j][k], dp1[i - 1][j][k - 1] + 1);
				if (j >= 2)
					dp1[i][j][k] = max(dp1[i][j][k], dp1[i][j -2][k] + 1);
				if (j && i >= 2)
					dp1[i][j][k] = max(dp1[i][j][k], dp1[i - 2][j - 1][k] + 1);
				if (j && k >= 2)
					dp1[i][j][k] = max(dp1[i][j][k], dp1[i][j - 1][k - 2] + 1);
			}
		}
	}
	forn (i, t) {
		cout << "Case #" << i + 1 <<": ";
		solve();
	}
	re 0;
}