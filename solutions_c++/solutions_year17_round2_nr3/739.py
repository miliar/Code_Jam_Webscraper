#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

double sp[111][111], ans[111][111], e[111], s[111], edge[111][111];
int n, q;


void work() {
	scanf("%d%d", &n, &q);
	for (int i = 1; i <= n; ++i) {
		scanf("%lf%lf", &e[i], &s[i]);
	}
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			scanf("%lf", &edge[i][j]);
		}
	}
	memcpy(sp, edge, sizeof(edge));
	for (int k = 1; k <= n; ++k) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (i == k || i == j || j == k) continue;
				if (sp[i][k] < -0.5 || sp[k][j] < -0.5) continue;
				if (sp[i][j] < -0.5) sp[i][j] = sp[i][k] + sp[k][j];
				else sp[i][j] = min(sp[i][j], sp[i][k] + sp[k][j]);
			}
		}
	}


	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			if (sp[i][j] > -0.5 && e[i] >= sp[i][j]) ans[i][j] = sp[i][j]/s[i];
			else ans[i][j] = -1;
		}
	}
	for (int k = 1; k <= n; ++k) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (i == k || i == j || j == k) continue;
				if (ans[i][k] < -0.5 || ans[k][j] < -0.5) continue;
				if (ans[i][j] < -0.5) ans[i][j] = ans[i][k] + ans[k][j];
				else ans[i][j] = min(ans[i][j], ans[i][k] + ans[k][j]);
			}
		}
	}
	/*
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j)  {
			printf("%lf ", ans[i][j]);
		}
		printf("\n");
	}
	*/
	/*
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			printf("%lf ", ans[i][j]);
		}
		printf("\n");
	}
	*/
	while (q--) {
		int u, t;
		scanf("%d%d", &u, &t);
		printf("%lf", ans[u][t]);
		if (q == 0) printf("\n");
		else printf(" ");
	}

}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		printf("Case #%d: ", tc);
		work();
	}
	
}