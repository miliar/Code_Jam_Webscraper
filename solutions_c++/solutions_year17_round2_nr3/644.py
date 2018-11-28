#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <iostream>

int T;

const int MN = 110;
int N, Q;
int U[MN], V[MN];

long long dst[MN][MN];
bool pos[MN][MN];
double ans[MN][MN];
int E[MN], S[MN];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);//*/
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		scanf("%d%d", &N, &Q);
		for(int i=1; i<=N; i++) {
			scanf("%d%d", &E[i], &S[i]);
		}
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				scanf("%I64d", &dst[i][j]);
			}
		}
		for(int i=0; i<Q; i++) {
			scanf("%d%d", &U[i], &V[i]);
		}
		// warshall
		for(int k=1; k<=N; k++) {
			for(int i=1; i<=N; i++) {
				for(int j=1; j<=N; j++) {
					if(dst[i][k] == -1 || dst[k][j] == -1) continue;
					if(dst[i][j] == -1 || dst[i][j] > dst[i][k] + dst[k][j]) {
						dst[i][j] = dst[i][k] + dst[k][j];
					}
				}
			}
		}
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				if(dst[i][j] != -1 && E[i] >= dst[i][j]) {
					ans[i][j] = (double)dst[i][j] / S[i];
					pos[i][j] = true;
				}
				else {
					ans[i][j] = 0.0f;
					pos[i][j] = false;
				}
			}
			dst[i][i] = 0;
			ans[i][i] = 0.0f;
			pos[i][i] = true;
		}
		for(int z=1; z<=N; z++) {
			for(int k=1; k<=N; k++) {
				for(int i=1; i<=N; i++) {
					for(int j=1; j<=N; j++) {
						// i~>k, k directly to j
						double now;
						if(dst[i][k] == -1 || dst[k][j] == -1) continue;
						if(!pos[i][k]) continue;
						//printf("try %d ~> %d, directly to %d...\n", i, k, j);
						if(E[k] >= dst[k][j]) {
							now = ans[i][k] + ((double)dst[k][j]/S[k]);
							//printf("(%d,%d) : try %d ~> %d, to %d: %f\n", i, j, i, k, j, now);
							if(!pos[i][j] || ans[i][j] > now) {
								ans[i][j] = now;
								pos[i][j] = true;
							}
						}
					}
				}
			}
		}
		printf("Case #%d:", tc);
		for(int i=0; i<Q; i++) {
			if(!pos[U[i]][V[i]]) fprintf(stderr, "not exist %d %d WTFFFFF\n", U[i], V[i]);
			printf(" %.7f", ans[U[i]][V[i]]);
		}
		printf("\n");
	}
	return 0;
}
