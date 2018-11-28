#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>

#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define iinf 2000000000
#define linf 2000000000000000000LL
#define MOD (1000000007)
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)

const string IMPOSSIBLE = "IMPOSSIBLE\n";
inline void case_print() {
	static int it = 0;
	it += 1;
	cout << "Case #" << it << ": ";
}

double dp[1111][1111] = {0};
double mdp[1111][1111] = {0};
int main() {
	ios_base::sync_with_stdio(0);
	freopen("A-large.in", "r",stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	while (T --> 0) {
		int n,k;
		cin >> n >> k;
		vector<pair<int, int> > a(n + 1);
		for (int i = 1; i <= n; i ++) {
			cin >> a[i].first >> a[i].second;
		}
		sort(a.begin() + 1, a.end(), greater<pair<int,int> >());
		for (int i = 0; i <= n; i ++) {
			for (int j = 0; j <= k; j ++) {
				dp[i][j]  = -1e6;
				mdp[i][j] = -1e6;
			}
			dp[i][0] = mdp[i][0] = 0.0;
		}
		for (int i = 1; i <= n; i ++) {
			dp[i][1] = 2.0*Pi*a[i].first * a[i].second + Pi * a[i].first * a[i].first;
			mdp[i][1] = max(mdp[i - 1][1], dp[i][1]);
			mdp[i][0] = max(mdp[i - 1][0], dp[i][0]);
		}
		
		for (int i = 1; i <= n; i ++) {
			for (int j = 2; j <= k; j ++) {
				dp[i][j] = 0.0;
				dp[i][j] = max(dp[i][j], mdp[i - 1][j - 1]);
				/*for (int t = i - 1; t >= 1; t --)
					dp[i][j] = max(dp[i][j], dp[t][j - 1]);*/
					
				dp[i][j] += 2.0 * Pi * a[i].first * a[i].second;
				mdp[i][j] = max(mdp[i - 1][j], dp[i][j]);
			}
		}
		double ans = 0.0;
		for (int i = 1; i <= n; i ++)
			ans = max(ans, dp[i][k]);
		case_print();
		cout.precision(9);
		cout << fixed << ans << endl;
	}
	
	return 0;
}
