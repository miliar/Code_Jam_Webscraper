#include <bits/stdc++.h>

using namespace std;

#define N 100
#define INF 0x3f3f3f3f3f3f3f3fll
#define DOUBLE_INF 1e18

typedef long long ll;

ll e[N + 1];
ll s[N + 1];
ll g[N + 1][N + 1];
ll dist[N + 1][N + 1];
double dp[N + 1][N * N + 1];
int n, v;

void floyd_warshall(){
	int i, j, k;

	for (i = 1; i <= n; i++){
		for (j = 1; j <= n; j++){
			dist[i][j] = (g[i][j] == -1 ? INF : g[i][j]);
		}

		dist[i][i] = 0;
	}

	for (i = 1; i <= n; i++){
		for (j = 1; j <= n; j++){
			for (k = 1; k <= n; k++){
				if (dist[j][i] + dist[i][k] < dist[j][k]){
					dist[j][k] = dist[j][i] + dist[i][k];
				}
			}
		}
	}
}

double solve(int u, int t){
	int i;

	if (u == v){
		return 0.0;
	}

	if (t == 0){
		return DOUBLE_INF;
	}

	if (dp[u][t] >= -1.0){
		return dp[u][t];
	}

	dp[u][t] = DBL_MAX;

	for (i = 1; i <= n; i++){
		if (i != u and e[u] >= dist[u][i]){
			dp[u][t] = min(dp[u][t], solve(i, t - 1) + ((double)dist[u][i] / (double)s[u]));
		}
	}

	return dp[u][t];
}

void memset_dp(){
	int i, j;

	for (i = 1; i <= n; i++){
		for (j = 1; j <= n * n; j++){
			dp[i][j] = -2.0;
		}
	}
}

int main(){
	int q, tc, ic, u, i, j;
	
	scanf("%d", &tc);
	
	for (ic = 1; ic <= tc; ic++){
		scanf("%d%d", &n, &q);

		for (i = 1; i <= n; i++){
			scanf("%lld%lld", e + i, s + i);
		}

		for (i = 1; i <= n; i++){
			for (j = 1; j <= n; j++){
				scanf("%lld", g[i] + j);
			}
		}

		floyd_warshall();

		printf("Case #%d:", ic);
		
		for (i = 1; i <= q; i++){
			scanf("%d%d", &u, &v);
			memset_dp();

			printf(" %.8lf", solve(u, n * n));
		}

		printf("\n");
	}

	return 0;
}