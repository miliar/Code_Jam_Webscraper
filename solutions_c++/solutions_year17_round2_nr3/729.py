/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

const int MN = 101;
const long long MVAL = 10000000000000000;

int h_dist[MN], h_speed[MN];
long long F[MN][MN];
double t[MN][MN];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;

	scanf("%d", &T);
	while (T--) {
		int n, q, i, j, k;
		scanf("%d %d", &n, &q);
		for (i = 0; i < n; i++) {
			scanf("%d %d", h_dist + i, h_speed + i);
		}

		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				scanf("%d", &F[i][j]);
				if (F[i][j] == -1) F[i][j] = MVAL;
			}
		}

		for (k = 0; k < n; k++) {
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++) {
					F[i][j] = min(F[i][j], F[i][k] + F[k][j]);
				}
			}
		}

		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				if (F[i][j] == MVAL || F[i][j] > h_dist[i]) {
					t[i][j] = MVAL;
					continue;
				}
				t[i][j] = (double)F[i][j] / h_speed[i];
			}
		}

		for (k = 0; k < n; k++) {
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++) {
					t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
				}
			}
		}

		printf("Case #%d:", K);
		K++;
		for (i = 0; i < q; i++) {
			int u, v;
			scanf("%d %d", &u, &v);
			--u, --v;
			printf(" %0.6f", t[u][v]);
		}
		puts("");
	}
	return 0;
}
