#include <stdio.h>
#include <algorithm>

void solve() {
	int n, q;
	int ttt[101][101];
	double dist[101];
	double speed[101];
	int from[101], to[101];
	scanf("%d %d", &n, &q);
	for (int i = 0; i < n; i++) {
		int e, s;
		scanf("%d %d", &e, &s);
		dist[i] = e;
		speed[i] = s;
	}
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < n; x++) {
			int val;
			scanf("%d", &val);
			ttt[y][x] = val;
		}
	}
	for (int i = 0; i < q; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		from[i] = u;
		to[i] = v;
	}

	double dp[101];
	dp[0] = 0;
	for (int i = 1; i < n; i++) {
		dp[i] = 1e300;
	}
	int curr = 0;
	int end = n - 1;
	while (curr < end) {
		double tot = dp[curr];
		double sp = speed[curr];
		double d = dist[curr];
		for (int i = 0; curr + i < n - 1; i++) {
			double next = ttt[curr + i][curr + i + 1] / sp;
			d -= ttt[curr + i][curr + i + 1];
			if (d < 0) break;
			tot += next;
			dp[curr + i + 1] = std::min(dp[curr + i + 1], tot);
		}

		curr++;
	}

	printf("%f\n", dp[n - 1]);
}

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
