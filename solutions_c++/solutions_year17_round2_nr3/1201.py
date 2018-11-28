#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
using namespace std;
const ll INF = 1e17;
int e[110];
int s[110];
long double d[110];
long double dp[110][110];
bool used[110];
inline void solve() {
	int n, q;
	scanf("%d%d", &n, &q);
	for (int i = 1; i <= n; i++) {
		scanf("%d%d", &e[i], &s[i]);
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			int x;
			scanf("%d",&x);
			dp[i][j] = x;
		}
		dp[i][i] = 0;
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			for (int k = 1; k <= n; k++) {
				if (dp[i][k] != -1 && dp[k][j] != -1) {
					if (dp[i][j] == -1) {
						dp[i][j] = dp[i][k] + dp[k][j];
					} else {
						dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
					}
				}
			}
		}
	}
	for (int qq = 1; qq <= q; qq++) {
		int uv, ue;
		scanf("%d%d", &uv, &ue);
		for (int i = 1; i <= n; i++) {
			d[i] = INF;
			used[i] = 0;
		}
		d[uv] = 0;
		for (int i = 1; i <= n; i++) {
			int cur = -1;
			for (int j = 1; j<= n; j++) {
				if (used[j] == true) {
					continue;
				}
				if (cur == -1 || d[cur] > d[j]) {
					cur = j;
				}
			}
			if (cur == -1) {
				break;
			}
			used[cur] = 1;
			for (int j = 1; j <= n; j++) {
				if (used[j]) {
					continue;
				}
				if (dp[cur][j] == -1) {
					continue;
				}
				if (dp[cur][j] <= e[cur]) {
					d[j] = min(d[j], dp[cur][j] / s[cur] + d[cur]);
				}
			}
		}
		cout << setprecision(9) << fixed << d[ue] << ' ';
	}
	cout << '\n';
}
int main() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		printf("Case #%d: ", test);
		solve();
	}
}
