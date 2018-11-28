#include <bits/stdc++.h>
using namespace std;
int T, N, Q, u, v;
double E[2000], S[2000];
double dis[120][120];
double mtt[120];
bool inqueue[120];
double dis1[120];
double calc(int u, int v) {
	//printf("calcing %d - %d\n", u, v);
	memset(inqueue, 0, sizeof inqueue);
	queue<int> nodes;
	nodes.push(u);
	inqueue[u] = 1;
	for(int i=1; i<=N; i++) {
		dis1[i] = 1e21;
	}
	dis1[u] = 0;
	/*for(int i=1; i<=N; i++) {
		printf("before: %d to %d: %.5lf\n", u, i, dis1[i]);
	}*/
	while(nodes.size()) {
		int n = nodes.front(); nodes.pop(); inqueue[n] = 0;
		for(int i=1; i<=N; i++) {
			//printf("seeking %d->%d\n", n, i);
			if (dis[n][i] <= E[n]) {
				//printf("ok, with dis1 %.6lf\n", dis1[i]);
				if (dis1[i] > dis1[n] + dis[n][i] / S[n]) {
					//printf("updated\n");
					dis1[i] = dis1[n] + dis[n][i] / S[n];
					if (!inqueue[i]) {
						nodes.push(i); inqueue[i] = 1;
					}
				}
			}
		} 
	}
	/*
	for(int i=1; i<=N; i++) {
		printf("%d to %d: %.5lf\n", u, i, dis1[i]);
	}*/
	return dis1[v];
}
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for(int Ks=1; Ks<=T; Ks++) {
		printf("Case #%d:", Ks);
		scanf("%d%d", &N, &Q);
		for(int i=1; i<=N; i++) {
			scanf("%lf%lf", E+i, S+i);
		}
		
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				scanf("%lf", &dis[i][j]);
				if (dis[i][j] < 0) dis[i][j] = 1e22;
			}
		}
	
		for(int k=1; k<=N; k++) {
			for(int i=1; i<=N; i++) {
				for(int j=1; j<=N; j++) {
					if (dis[i][k] + dis[k][j] < dis[i][j]) {
						dis[i][j] = dis[i][k] + dis[k][j];
					}
				}
			}
		}
			/*
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				printf("%.1f ", dis[i][j] < 1e10 ? dis[i][j] : -1);
			}
			puts("");
		}
		puts("");*/
		
		
		for(int i=0; i<Q; i++) {
			scanf("%d%d", &u, &v);
			printf(" %.12lf", calc(u, v));
		}
		puts("");
	}
}
