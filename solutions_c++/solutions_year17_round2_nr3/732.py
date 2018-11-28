#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cassert>
using namespace std;


const double eps = 1e-8;
const double pi = acos(-1.0);

const int N = 1005;
const double INF = 1e60;

long double e[N], s[N];
long double d[N][N];

bool vis[N];

void floyd(int n) {
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) {
                if (d[i][k] == INF || d[k][j] == INF) continue;
                if (d[i][j] > d[i][k] + d[k][j])
                    d[i][j] = d[i][k] + d[k][j];
            }
}

long double g[N][N];
void floyd2(int n) {
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) {
                if (g[i][k] == INF || g[k][j] == INF) continue;
                if (g[i][j] > g[i][k] + g[k][j])
                    g[i][j] = g[i][k] + g[k][j];
            }
}

int n;


double makeG(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            g[i][j]=INF;
            if (d[i][j] > e[i]) {
                continue;
            }
            g[i][j] = d[i][j] / s[i];
        }
    }
}


int alice[N], bob[N];
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for (int cas = 1; cas <= T; cas++) {
        memset(vis, false, sizeof vis);
        int  q;
        cin >> n >> q;

        for (int i = 1; i <= n; i++) {
            cin >> e[i] >> s[i];
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> d[i][j];
                if (d[i][j] == -1) {
                    d[i][j]=INF;
                }
            }
        }

        for (int i = 1; i <= q; i++) {
            cin >> alice[i] >> bob[i];
        }

        floyd(n);

        makeG(n);

        floyd2(n);

        printf("Case #%d:", cas);

        for (int i = 1; i <= q; i++) {
            printf(" %.8Lf", g[alice[i]][bob[i]]);
        }

        puts("");
    }
    return 0;
}

