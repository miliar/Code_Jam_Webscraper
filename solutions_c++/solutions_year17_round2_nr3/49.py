#include <bits/stdc++.h>

#define debug(x) cout << #x" = " << x;

#define st first
#define nd second

using namespace std;
using namespace placeholders;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;

const int MAXN = 1E2 + 10;

int n, m;
int e[MAXN], s[MAXN];
ll a[MAXN][MAXN];
double b[MAXN][MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i)
			scanf("%d%d\n", e + i, s + i);

		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				scanf("%lld", a[i] + j);

		for (int k = 1; k <= n; ++k)
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= n; ++j){
					if (a[i][k] >= 0 && a[k][j] >= 0){
						ll t = a[i][k] + a[k][j];
						if (a[i][j] == -1 || a[i][j] > t)
							a[i][j] = t;
					}
				}

		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j){
				if (a[i][j] >= 0 && a[i][j] <= e[i])
					b[i][j] = 1.0 * a[i][j] / s[i];
				else
					b[i][j] = -1;
			}

		for (int k = 1; k <= n; ++k)
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= n; ++j){
					if (b[i][k] > -0.5 && b[k][j] > -0.5){
						double t = b[i][k] + b[k][j];
						if (b[i][j] < -0.5 || b[i][j] > t)
							b[i][j] = t;
					}
				}

		for (int u, v, i = 0; i < m; ++i){
			scanf("%d%d", &u, &v);
			printf(" %.12f", b[u][v]);
		}
		puts("");
	}
	return 0;
}
