#include<cstdio>

int T, n, q, e[102], s[102], d[102][102], u[102], v[102];
long long dis[102];
double dp[102][102];
bool found[102][102];

double min(double x, double y) {
	return x < y ? x : y;
}

double find(int L, int R) {
	if (found[L][R]) return dp[L][R];
	found[L][R] = true;
	if (e[L] >= dis[R] - dis[L]) dp[L][R] = 1. * (dis[R] - dis[L]) / s[L];
	for (int i = L + 1; i < R; i++) dp[L][R] = min(dp[L][R], find(L, i) + find(i, R));
	return dp[L][R];
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int Test = 1; Test <= T; Test++) {
		scanf("%d %d", &n, &q);
		for (int i = 1; i <= n; i++) scanf("%d %d", &e[i], &s[i]);
		for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) scanf("%d", &d[i][j]);
		for (int i = 0; i < q; i++) scanf("%d %d", &u[i], &v[i]);
		
		// small only
		for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) {
			dp[i][j] = 1e15;
			found[i][j] = false;
		}
		for (int i = 2; i <= n; i++) dis[i] = dis[i - 1] + d[i - 1][i];
		printf("Case #%d: %lf\n", Test, find(1, n));
		// small only
	}
}
