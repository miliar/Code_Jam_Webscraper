#include <bits/stdc++.h>
using namespace std;

// why am I so weak

int n, q;
int e[155], s[155];

long long c[155][155];

bool used[155][155];
double d[155][155];
double res[155][155];

int main() {
	int _t;

	scanf("%d", &_t);

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d:", _ + 1);

		scanf("%d %d", &n, &q);

		for (int i = 0; i < n; i++) {
			scanf("%d %d", &e[i], &s[i]);
		}

		for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
			scanf("%lld", &c[i][j]);
		}

		for (int i = 0; i < n; i++) c[i][i] = 0;

		for (int k = 0; k < n; k++) for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
			if (~c[i][k] && ~c[k][j]) {
				if (c[i][j] < 0) c[i][j] = c[i][k] + c[k][j];
				c[i][j] = min(c[i][j], c[i][k] + c[k][j]);
			}
		}

		for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) d[i][j] = 1e20;

		for (int i = 0; i < n; i++) d[i][i] = 0.;

		for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
			if (c[i][j] >= 0 && c[i][j] <= 1ll * e[i]) {
				d[i][j] = min(d[i][j], 1. * c[i][j] / s[i]);
			}
		}

		for (int k = 0; k < n; k++) {
			for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}

		while (q--) {
			int x, y;
			scanf("%d %d", &x, &y);
			x--, y--;

			printf(" %.10lf", d[x][y]);
		}

		puts("");
	}

	return 0;
}

