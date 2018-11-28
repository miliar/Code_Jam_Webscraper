#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
//const double PI = atan(1) * 4;



const int SZ = 103;
const ll INF = 1e18;

int N, Q;
ll E[SZ], S[SZ];
ll D[SZ][SZ];
double T[SZ][SZ];


int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);

		scanf("%d%d", &N, &Q);
		for (int i=1; i<=N; i++) scanf("%lld%lld", &E[i], &S[i]);
		for (int i=1; i<=N; i++) for (int j=1; j<=N; j++)
			scanf("%lld", &D[i][j]);

		for (int i=1; i<=N; i++) for (int j=1; j<=N; j++) if (D[i][j] == -1)
			D[i][j] = INF;
		for (int k=1; k<=N; k++) for (int i=1; i<=N; i++) for (int j=1; j<=N; j++)
			D[i][j] = min(D[i][j], D[i][k] + D[k][j]);

		for (int i=1; i<=N; i++) for (int j=1; j<=N; j++)
			T[i][j] = D[i][j] <= E[i] ? (double)D[i][j] / S[i] : INF;
		for (int k=1; k<=N; k++) for (int i=1; i<=N; i++) for (int j=1; j<=N; j++)
			T[i][j] = min(T[i][j], T[i][k] + T[k][j]);

		FOR(zz, Q) {
			int u, v; scanf("%d%d", &u, &v);
			printf("%.10lf ", T[u][v]);
		}
		puts("");


	}


	return 0;
}
