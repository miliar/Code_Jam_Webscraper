#include<bits/stdc++.h>
using namespace std;
const int maxn = 205;
int A[maxn], B[maxn];
long long C[maxn][maxn];
double dist[maxn][maxn];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    int T; 
	scanf("%d",&T);
    for(int cas = 1; cas <= T; cas ++) {
        int n, q; 
		scanf("%d%d", &n, &q);
        for(int i = 1; i <= n; i ++) {
            scanf("%d%d", &A[i], &B[i]);
        }
        for(int i = 1; i <= n; i ++) {
            for(int j = 1; j <= n; j ++) {
                scanf("%lld", &C[i][j]);
                if (C[i][j] != -1 && C[i][j] <= A[i]){
                    dist[i][j] = C[i][j] * 1.0 / B[i];
                }
                else{
                    dist[i][j] = -1;
                }
             //   printf("__dist[%d][%d] = %f____%d\n", i, j, dist[i][j], B[i]);
            }
        }
        for(int k = 1; k <= n; k ++) {
            for(int i = 1; i <= n; i ++) {
                if (C[i][k] == -1) continue;
                for(int j = 1; j <= n; j ++) {
                    if (C[k][j] == -1) continue;
                    if (C[i][j] == -1 || C[i][j] > C[i][k] + C[k][j]) {
                        C[i][j] = C[i][k] + C[k][j];
                        if (C[i][j] <= A[i] && (dist[i][j] < -0.5 || dist[i][j] > C[i][j]*1.0 / B[i])){
                            dist[i][j] = C[i][j] * 1.0 / B[i];
                        }
                    }

                }
            }
        }
        for(int k = 1; k <= n; k ++) {
            for(int i = 1; i <= n; i ++) {
                if (dist[i][k] > -0.5) {
                    for(int j = 1; j <= n; j ++) {
                        if (dist[k][j] > -0.5) {
                            if (dist[i][j] < -0.5 || dist[i][j] > dist[i][k] + dist[k][j]) {
                                dist[i][j] = dist[i][k] + dist[k][j];
                            }
                        }
                    }
                }
            }
        }
        printf("Case #%d: ", cas);
        for(int i = 0, u, v; i < q; i ++) {
            scanf("%d%d", &u, &v);
            printf("%.10f%c", dist[u][v], i == q - 1 ? '\n':' ');
        }
    }
    return 0;
}

