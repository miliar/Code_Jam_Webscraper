#include <bits/stdc++.h>
using namespace std;
#define ll long long
int T, n, q, a[105][105], d[105], s[105], u, v;
ll p[105];
double dp[105];
void solve(int test) {
	memset(dp, 0, sizeof dp);
	scanf("%d %d", &n, &q);
	for (int i=1; i<=n; i++) scanf("%d %d", &d[i], &s[i]);
	for (int i=1; i<=n; i++) {
		for (int j=1; j<=n; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	for (int i=2; i<=n; i++) {
		p[i]=p[i-1]+a[i-1][i];
	}
	while (q--) {
		scanf("%d %d", &u, &v);
		dp[0]=0;
		for (int i=2; i<=n; i++) {
			dp[i]=9223372036854775807;
			for (int j=1; j<i; j++) {
				//printf("%d\n", p[i]-p[j]);
				//printf("%.10lf %.10lf\n", dp[j], 1.0*(p[i]-p[j])/s[j]);
				if (p[i]-p[j]<=d[j]) dp[i]=min(dp[i], dp[j]+1.0*(p[i]-p[j])/s[j]);
			}
		}
	}
	printf("Case #%d: ", test);
	printf("%.10lf\n", dp[n]);
}
int main () {
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
