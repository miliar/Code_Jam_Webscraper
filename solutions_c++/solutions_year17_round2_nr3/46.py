#include<stdio.h>
#include<string.h>
int n, q;
long long int e[110];
long long int s[110];
long long int d[110][110];
double res[110][110];
int qry[110][2];
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%d%d", &n, &q);
		for (int i = 0; i < n; i++) {
			scanf("%lld%lld", &e[i], &s[i]);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%lld", &d[i][j]);
				if (d[i][j] == -1)d[i][j] = 1e18;
			}
		}
		for (int i = 0; i < q; i++) {
			scanf("%d%d", &qry[i][0], &qry[i][1]);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {
					if (d[j][k] > d[j][i] + d[i][k])d[j][k] = d[j][i] + d[i][k];
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (d[i][j] > e[i])res[i][j] = 1e99;
				else res[i][j] = ((double)d[i][j]) / s[i];
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {
					if (res[j][k] > res[j][i] + res[i][k])res[j][k] = res[j][i] + res[i][k];
				}
			}
		}
		printf("Case #%d:", tc);
		for (int i = 0; i < q; i++) {
			printf(" %.10lf", res[qry[i][0] - 1][qry[i][1] - 1]);
		}
		printf("\n");
	}
	return 0;
}
