#include <cstdio>
#include <iostream>

using namespace std;

#define INF 100000000000007

int t, n, q, e[200], a, b, x, s[200];
long long d[200][200];
double d2[200][200];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &t);

	for (int it = 1; it <= t; ++it) {
		scanf("%d%d", &n, &q);

		for (int i = 1; i <= n; ++i) {
			scanf("%d%d", &e[i], &s[i]);
		}

		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				scanf("%d", &x);
				if (x == -1)
					d[i][j] = INF;
				else
					d[i][j] = x;
			}
		}

		for (int k = 1; k <= n; ++k)
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= n; ++j)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (j != i && d[i][j] <= e[i]) {
					d2[i][j] = d[i][j] / (0.0 + s[i]);
				} else {
					d2[i][j] = INF;
				}

		for (int k = 1; k <= n; ++k)
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= n; ++j)
					d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j]);

		printf("Case #%d: ", it);
		for (int i = 1; i <= q; ++i) {
			scanf("%d%d", &a, &b);
			printf("%.10lf ", d2[a][b]);
		}

		puts("");
	}
}