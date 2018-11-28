#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef double LF;

const LF INF = 1e18;

const int maxN = 100 + 5, maxQ = 100 + 5;

int T, n, q;
int S[maxN], E[maxN], d[maxN][maxN], u[maxQ], v[maxQ];

LL dis[maxN];

LF ans[maxQ], f[maxN];

int main() {
    //freopen("3.in", "r", stdin);
    //freopen("3.txt", "w", stdout);
    scanf("%d", &T);
    for (int testCase = 1; testCase <= T; ++testCase) {
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; ++i)
            scanf("%d%d", &E[i], &S[i]);
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                scanf("%d", &d[i][j]);
        for (int i = 1; i <= q; ++i)
            scanf("%d%d", &u[i], &v[i]);
        printf("Case #%d: ", testCase);
        f[1] = 0;
        dis[1] = 0;
        for (int i = 2; i <= n; ++i)
            dis[i] = dis[i - 1] + d[i - 1][i];
        for (int i = 2; i <= n; ++i) {
            f[i] = INF;
            for (int j = 1; j < i; ++j) {
                if (dis[i] - dis[j] <= E[j]) {
                    f[i] = min(f[i], f[j] + (LF)(dis[i] - dis[j]) / (LF)S[j]);
                }
            }
        }
        printf("%.7f\n", f[n]);
    }
    return 0;
}
