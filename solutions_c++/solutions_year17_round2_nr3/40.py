#include <bits/stdc++.h>

using namespace std;

const int MX = 100;
const long long INF = 1e13;

long long d[MX][MX], e[MX], s[MX];
long double D[MX][MX];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, q;
		scanf("%d %d", &n, &q);
		for (int i = 0; i < n; i++) scanf("%lld %lld", e + i, s + i);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				scanf("%lld", &d[i][j]);
				if (d[i][j] < 0) d[i][j] = INF;
				if (i == j) d[i][j] = 0;
			}
		
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (d[i][j] > e[i]) D[i][j] = INF;
				else D[i][j] = d[i][j] / (long double)s[i];

		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
		
		printf("Case #%d:", t);
		while (q--) {
			int u, v;
			scanf("%d %d", &u, &v);
			printf(" %.15lf", (double)D[u - 1][v - 1]);
		}
		printf("\n");
	}

	return 0;
}
