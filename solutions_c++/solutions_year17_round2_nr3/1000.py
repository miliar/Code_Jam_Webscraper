#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 7;
const double INF = 1e100;

double f[N];
double dist[N][N];
int n, q, reach[N], speed[N], visit[N];

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		static int testCount = 0;
		printf("Case #%d:", ++testCount);
		scanf("%d %d", &n, &q);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &reach[i], &speed[i]);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%lf", &dist[i][j]);
				if (dist[i][j] < 0) {
					dist[i][j] = INF;
				}
			}
		}
		for (int i = 0; i < n; i++) dist[i][i] = 0;
		for (int k = 0; k < n; k++) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}
		for (int i = 0; i < q; i++) {
			int s, t;
			scanf("%d %d", &s, &t);
			s--, t--;
			for (int j = 0; j < n; j++) {
				f[j] = INF;
				visit[j] = false;
			}
			f[s] = 0;
			for (int t = 1; t <= n; t++) {
				double minv = INF;
				int who = -1;
				for (int j = 0; j < n; j++) {
					if (!visit[j] && f[j] < minv) {
						minv = f[j];
						who = j;
					}
				}
				assert(who != -1);
				visit[who] = true;
				for (int j = 0; j < n; j++) {
					if (!visit[j] && dist[who][j] <= reach[who]) {
						f[j] = min(f[j], f[who] + dist[who][j] / speed[who]);
					}
				}
			}
			printf(" %.10f", f[t]);
		}
		puts("");
	}
	return 0;
}
