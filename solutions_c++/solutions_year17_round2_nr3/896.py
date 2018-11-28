#include <bits/stdc++.h>

using namespace std;

const double INF = 10e11;
const int MAXN = 100;
double enduranceDist[MAXN+2];
double speed[MAXN+2];
double dist[MAXN+2][MAXN+2];
double distRevo[MAXN+2][MAXN+2];

int main() {
	int ntc; scanf("%d", &ntc);
	for (int tc = 0; tc < ntc; tc++) {
		int n, q; scanf("%d%d", &n, &q);

		for (int i = 0; i < n; i++) {
			scanf("%lf%lf", &enduranceDist[i], &speed[i]);
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%lf", &dist[i][j]);
				if (dist[i][j] == -1) {
					dist[i][j] = INF;
				}
			}
		}

		for (int k = 0; k < n; k++) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (dist[i][k] + dist[k][j] < dist[i][j]) {
						dist[i][j] = dist[i][k] + dist[k][j];
					}
				}
			}
		}
/*
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				printf("%.2lf ", dist[i][j]);
			}
			printf("\n");
		}
*/
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (enduranceDist[i] >= dist[i][j]) {
					distRevo[i][j] = dist[i][j]/speed[i];
				} else {
					distRevo[i][j] = INF;
				}
			}
		}

		for (int k = 0; k < n; k++) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (distRevo[i][k] + distRevo[k][j] < distRevo[i][j]) {
						distRevo[i][j] = distRevo[i][k] + distRevo[k][j];
					}
				}
			}
		}

		printf("Case #%d:", tc+1);
		for (int iq = 0; iq < q; iq++) {
			int u, v; scanf("%d%d", &u, &v);
			u--; v--;

			printf(" %.8lf", distRevo[u][v]);
		}
		printf("\n");
	}
}