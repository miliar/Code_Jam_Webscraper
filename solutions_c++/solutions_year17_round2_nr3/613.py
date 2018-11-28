#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <queue>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)
#define N 111

int T, n, q, u, v, s[N], e[N];
long long d[N][N];
double ans[N];

void dfs(int x, double t) {
    if (t > ans[x]) return;
    ans[x] = min(ans[x], t);
    if (x != v-1)
    rep(i, n)
        if (d[x][i] + 1 && d[x][i] <= e[x])
            dfs(i, t + d[x][i] / (double)s[x]);
}

void solve() {
    scanf("%d%d", &n, &q);
    rep(i, n) scanf("%d%d", e+i, s+i);
    rep(i, n) rep(j, n) scanf("%I64d", &d[i][j]);
    rep(k, n) rep(i, n) rep(j, n) if (i-j && d[i][k]+1 && d[k][j]+1) if (d[i][j] == -1 || d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];

    rep(i, q) {
        scanf("%d%d", &u, &v);
        rep(_i, n) ans[_i] = 1ll << 60;
        ans[u-1] = 0;
        dfs(u-1, 0);
        printf("%.9f", ans[v-1]);
        if (i == q-1) puts(""); else putchar(' ');
    }
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
