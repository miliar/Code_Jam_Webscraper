#include <bits/stdc++.h>
using namespace std;

typedef long long lld;

int T, N, Q;
int E[104], S[104];
lld D[104][104];
long double w[104][104];

int main()
{
	for (scanf("%d", &T);T--;){
		scanf("%d%d", &N, &Q);
		for (int i=1;i<=N;i++) scanf("%d%d", E+i, S+i);
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++){
			scanf("%lld", D[i]+j);
			if (D[i][j] == -1) D[i][j] = 1e18;
			if (i == j) D[i][j] = 0;
		}
		for (int k=1;k<=N;k++) for (int i=1;i<=N;i++) for (int j=1;j<=N;j++){
			D[i][j] = min(D[i][j], D[i][k]+D[k][j]);
		}
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++){
			if (D[i][j] <= E[i]) w[i][j] = (long double)D[i][j] / S[i];
			else w[i][j] = 1e100;
		}
		for (int k=1;k<=N;k++) for (int i=1;i<=N;i++) for (int j=1;j<=N;j++){
			w[i][j] = min(w[i][j], w[i][k]+w[k][j]);
		}
		static int ts = 0;
		printf("Case #%d: ", ++ts);
		for (int i=1;i<=Q;i++){
			int a, b; scanf("%d%d", &a, &b);
			printf(" %.8Lf", w[a][b]);
		} puts("");
	}
}