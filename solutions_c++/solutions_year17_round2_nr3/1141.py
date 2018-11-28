#include <bits/stdc++.h>
using namespace std;

double E[105], S[105], D[105][105], dp[105];

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.o", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		int N, Q;
		scanf("%d %d", &N, &Q);
		for (int i = 0; i < N; i++) {
			scanf("%lf %lf", &E[i], &S[i]);
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%lf", &D[i][j]);
			}
		}
		int U, V;
		scanf("%d %d", &U, &V);
		for (int i = 1; i < N; i++) {
			dp[i] = -1;
		}
		for (int i = 0; i < N - 1; i++) {
			double ret = 0;
			for (int j = i; j < N - 1; j++) {
				ret += D[j][j + 1];
				if (ret >= E[i] + 1) break;
				if (dp[j + 1] == -1) {
					dp[j + 1] = ret / S[i] + dp[i];
				} else {
					dp[j + 1] = min(ret / S[i] + dp[i], dp[j + 1]);
				}
			}
		}
		printf("%lf\n", dp[N - 1]);
	}
}