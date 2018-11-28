#include <bits/stdtr1c++.h>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef pair<ld, ld> pdd;
typedef complex<ld> pt;

const int N = 1005;
int n;
ld memo[N][N], pi = acos(-1.0);
pdd a[N];
ld dp(int i, int j) {
	ld r = a[i].first, h = a[i].second;
	if (memo[i][j] > 0) {
		return memo[i][j];
	} else if (j == 0) {
		return 0;
	}
	
	ld& ans = memo[i][j] = 0;
	for (int l = i+1; l <= n; l++) {
		ld r_ = a[l].first, h_ = a[l].second;
		if (i == 0) r = r_;
		ans = max(ans, dp(l, j-1) + 2 * pi * r_ * h_ + pi * (r * r - r_ * r_));
		ans = max(ans, 2 * pi * r_ * h_ + pi * r * r);
	}
	return ans;
}

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
		int k; cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> a[i].first >> a[i].second;
		}
		a[n].first = 1e99, a[n].second = 0;
		sort(a, a+n+1);
		reverse(a, a+n+1);
		a[0].first = a[1].first;
		
		memset(memo, 0, sizeof memo);
        cout << "Case #" << ca << ": " << fixed << setprecision(16) << dp(0, k) << endl;;
    }
	return 0;
}