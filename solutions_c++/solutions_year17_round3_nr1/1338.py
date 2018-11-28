/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
*/
#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define sp " "
#define fi first
#define se second
#define MOD 1000000007
#define N 1007
#define int long long
#define pie 3.1415926535897932
#define Mask(x) (1ll<<(x))
#define lnode (node<<1)
#define rnode ((node<<1)+1)
#define mid ((l+r)>>1)
using namespace std;
typedef pair<int, int> ii;
typedef long long ll;

int t, test, n, k, dp[N][N];
ii a[N];
long double ans;

signed main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> t; 
	for(int test = 1; test <=t; ++test){
		cin >> n >> k; memset(dp, 0, sizeof dp);
		for(int i=1; i<=n; ++i) cin >> a[i].fi >> a[i].se;
		sort(a+1, a+n+1, greater<ii>());
		for(int i=1; i<=n; ++i){
			dp[i][1] = a[i].fi * a[i].fi + 2 * a[i].fi * a[i].se;
			for(int j=1; j<=k; ++j)
				dp[i][j] = max(dp[i][j], max(dp[i-1][j], dp[i-1][j-1] + 2 * a[i].fi * a[i].se));
		}
		ans = dp[n][k] * pie;
		cout << "Case #" << test << ": " << fixed << setprecision(9) << ans << endl;
	}
	return 0;
}