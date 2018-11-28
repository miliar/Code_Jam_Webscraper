#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;

#define fi first
#define se second

const int oo = 1e9;
const double PI = M_PI;
#define maxn 1011

double dp[1011][1011][2];
pair<double, double> a[maxn];

int main(){
	freopen("a.inp", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int n, k;
		cin >> n >> k;

		memset (dp, 0, sizeof (dp));

		for (int i = 1; i <= n; i++){
			cin >> a[i].fi >> a[i].se;
		}
		sort (a + 1, a + n + 1);
		reverse (a + 1, a + n + 1);
		double ret = 0;
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= k; j++){
				if (j == 1)
					dp[i][j][1] += a[i].fi * a[i].fi * PI;
				dp[i][j][0] = max (dp[i-1][j][0], dp[i-1][j][1]);
				dp[i][j][1] += max (dp[i-1][j-1][1], dp[i-1][j-1][0]) + a[i].fi * a[i].se * 2 * PI;
				if (j == k) ret = max (ret, max (dp[i][j][1], dp[i][j][0]));
			}
		}
		printf ("Case #%d: %.9f\n", t, ret);
	}

    return 0;
}
