#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int, int> II;

const int N = 100 + 10;
const LL INF = 1e16;
int n, q, E[N], S[N];
LL w[N][N];
double d[N];
bool fre[N];

double Compute(int s, int t) {
    for (int i = 0; i <= n; ++i) d[i] = INF, fre[i] = true; d[s] = 0;
    while (1) {
        int u = 0;
        for (int i = 1; i <= n; ++i)
            if (fre[i] && d[u] > d[i]) u = i;
        if (u == 0) break; fre[u] = false;
        for (int v = 1; v <= n; ++v) {
            if (fre[v] == false) continue;
            if (w[u][v] <= E[u]) d[v] = min(d[v], d[u] + (double) w[u][v] / S[u]);
        }
    }
    return d[t];
}

int main() {
    freopen("C.inp", "r", stdin);
    freopen("C.out", "w", stdout);
    int TC; scanf("%d", &TC);
    for (int testID = 1; testID <= TC; ++testID) {
        printf("Case #%d: ", testID);
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; ++i) scanf("%d%d", &E[i], &S[i]);
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                int a; scanf("%d", &a);
                w[i][j] = (a == -1) ? INF : a;
            }
            w[i][i] = 0;
        }
        for (int k = 1; k <= n; ++k)
            for (int i = 1; i <= n; ++i)
                for (int j = 1; j <= n; ++j)
                    w[i][j] = min(w[i][j], w[i][k] + w[k][j]);

        while (q--) {
            int s, t; scanf("%d%d", &s, &t);
            printf("%.10lf ", Compute(s, t));
        }
        puts("");
    }
    return 0;
}
