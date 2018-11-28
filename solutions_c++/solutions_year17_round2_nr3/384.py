#include <bits/stdc++.h>
using namespace std;
const int MAXN = 105;
const double INF = 1e15;

int n, q, d[MAXN], s[MAXN];
double g[MAXN][MAXN];

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int i, j, k, tmp, st, ed, testcase, kase = 0;
	scanf("%d", &testcase);
	while(testcase --){
		scanf("%d%d", &n, &q);
		for(i = 1; i <= n; ++ i)
			scanf("%d%d", &d[i], &s[i]);
		for(i = 1; i <= n; ++ i)
			for(j = 1; j <= n; ++ j){
				scanf("%d", &tmp);
				if(tmp == -1) g[i][j] = INF;
				else g[i][j] = tmp;
				if(i == j) g[i][i] = 0.0;
			}
		for(k = 1; k <= n; ++ k)
			for(i = 1; i <= n; ++ i)
				for(j = 1; j <= n; ++ j)
					if(g[i][j] > g[i][k] + g[k][j])
						g[i][j] = g[i][k] + g[k][j];
		for(i = 1; i <= n; ++ i)
			for(j = 1; j <= n; ++ j)
				if(d[i] >= g[i][j])
					g[i][j] = g[i][j] * 1.0 / s[i];
				else g[i][j] = INF;
		for(k = 1; k <= n; ++ k)
			for(i = 1; i <= n; ++ i)
				for(j = 1; j <= n; ++ j)
					if(g[i][j] > g[i][k] + g[k][j])
						g[i][j] = g[i][k] + g[k][j];
		printf("Case #%d:", ++ kase);
		for(i = 1; i <= q; ++ i){
			scanf("%d%d", &st, &ed);
			printf(" %.10lf", g[st][ed]);
		} printf("\n");
	}
	return 0;
}
