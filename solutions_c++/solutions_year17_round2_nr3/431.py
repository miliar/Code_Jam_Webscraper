#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;

const int MaxN = 100;
const LL INF = 1LL << 60;
LL gdis[MaxN + 5][MaxN + 5], e[MaxN + 5], v[MaxN + 5];
double gtime[MaxN + 5][MaxN + 5];
int n, Q, T;

void Init()
{
	scanf("%d%d", &n, &Q);
	for (int i = 1; i <= n; i++) scanf("%lld%lld", &e[i], &v[i]);
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			scanf("%lld", &gdis[i][j]);
			if (gdis[i][j] == -1) gdis[i][j] = INF;
		}
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				gdis[i][j] = min(gdis[i][j], gdis[i][k] + gdis[k][j]);
}

void Solve(int cas)
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (gdis[i][j] <= e[i]) {
				gtime[i][j] = gdis[i][j] * 1.0 / v[i];
			}
			else gtime[i][j] = INF;
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				gtime[i][j] = min(gtime[i][j], gtime[i][k] + gtime[k][j]);
	printf("Case #%d: ", cas);
	for (int i = 1; i <= Q; i++) {
		int u, v;
		scanf("%d%d", &u, &v);
		printf("%.10lf ", gtime[u][v]);
	}
	printf("\n");
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		Init();
		Solve(cas);
	}
	fclose(stdin);
	fclose(stdout);
}
