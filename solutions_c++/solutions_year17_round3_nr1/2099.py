#include <bits/stdc++.h>
#define endl '\n'
#define mod 1000000007
typedef long long LL;
const int maxn = 1e3 + 2;
const LL inf = 1e18;
using namespace std;
int t, n, k;
double dp[maxn][maxn];
struct data{
		double r, h;
}a[maxn];

bool comp(const data& i, const data& j) {
	return i.r > j.r;
}

inline double csa(int idx) {
	return (2.0 * M_PI * a[idx].r * a[idx].h);
}

inline double sa(int idx) {
	return (M_PI * a[idx].r * a[idx].r);
}

double solve(int curr, int done) {
	if(done == k) {
		// cout << curr << endl;
		return csa(curr) + sa(curr);
	}
	for(int i = curr + 1; i <= n; i++) {
		dp[curr][done] = max(dp[curr][done], max(solve(i, done + 1) + csa(curr) + (sa(curr) - sa(i)), solve(i, done)));
	}
	return dp[curr][done];
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> n >> k;
		for(int i = 1; i <= n; i++) {
			cin >> a[i].r >> a[i].h;
		}
		cout.precision(20);
		if(k == 1) {
			double ans = 0;
			for(int i = 1; i <= n; i++) ans = max(ans, csa(i) + sa(i));
			cout << "Case #" << i << ": " << ans << endl;
			continue;
		}
		sort(a + 1, a + n + 1, comp);
		solve(1, 1);
		cout << "Case #" << i << ": " << dp[1][1] << endl;
		for(int i = 0; i < maxn; i++) for(int j = 0; j < maxn; j++) dp[i][j] = 0;
	}
	return 0;
}
