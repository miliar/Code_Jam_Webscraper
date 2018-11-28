#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#define ll long long
using namespace std;
const int N = 110;
ll d[N][N];
double t[N][N];
int n, Q;
int E[N], S[N];
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d", &n, &Q);
		for (int i = 1; i <= n; i++) scanf("%d%d", &E[i], &S[i]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				cin >> d[i][j];
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++) if(d[i][k] != -1)
				for (int j = 1; j <= n; j++) if(d[k][j] != -1) {
					if(d[i][j] == -1) d[i][j] = d[i][k] + d[k][j];
					else d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
				}
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				if(d[i][j] == -1 || d[i][j] > E[i]) t[i][j] = -1;
				else t[i][j] = d[i][j] * 1.0 / S[i];
			}
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++) if(t[i][k] != -1) {
				for (int j = 1; j <= n; j++) if(t[k][j] != -1) {
					if(t[i][j] == -1) t[i][j] = t[i][k] + t[k][j];
					else t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
				}
			}
		printf("Case #%d:", cas);
		int u, v;
		while(Q--) {
			scanf("%d%d", &u, &v);
			printf(" %.7lf", t[u][v]);
		}
		puts("");
	}
	return 0;
}