#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=(l);i<(n);++i)
#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/priority_queue.hpp>
using namespace std;
// using namespace __gnu_pbds;
typedef long double lf;
#define N 1010
const lf pi = acos(-1);
struct { int r, h; } p[N];
int n, k;
lf dp[N][N], ans;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	// cout << setprecision(15) << fixed << pi << endl;
	int t;
	cin >> t;
	Fl(cases, 1, t+1) {
		cout << "Case #" << cases << ": ";
		cin >> n >> k;
		memset(dp, 0, sizeof(dp));
		ans = 0.0;
		F(n) { cin >> p[i].r >> p[i].h; }
		Fi(u, n) {
			dp[u][1] = pi * (lf)p[u].r * (lf)p[u].h * (lf)2 + (lf)p[u].r * (lf)p[u].r * pi;
			ans = max(ans, dp[u][1]);
			F(n) if (i != u) for(int j = k - 1 ; j >= 1 ; --j) {
				lf tmp = dp[u][j] + pi * (lf)p[i].r * (lf)p[i].h * (lf)2;
				dp[u][j+1] = max(dp[u][j+1], tmp);
				ans = max(ans, dp[u][j+1]);
			}
		}
		cout << setprecision(9) << fixed << ans + 1e-20 << '\n';
	}
}