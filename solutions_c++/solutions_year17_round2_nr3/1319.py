#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 105;

LL d[N][N];
double t[N][N], a[N][N];
int ee[N], ss[N];
 bool mark[N];

void solve(int nt) {
    int n, q;
    scanf("%d%d", &n, &q);

    for (int i = 1; i <= n; i++) {
        scanf("%d%d", ee+i, ss+i);
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            scanf("%lld", &d[i][j]);
        }
    }

    for (int k = 1; k <= n; k++)
    for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
        if (d[i][k] > 0 && d[k][j] > 0 && (d[i][j] < 0 || d[i][j] > d[i][k] + d[k][j]))
            d[i][j] = d[i][k] + d[k][j];

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++)
            if (d[i][j] <= ee[i])
                t[i][j] = d[i][j] * 1.0 / ss[i];
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            a[i][j] = 1e14;
            mark[j] = true;
        }
        a[i][0] = 1e18;
        a[i][i] = 0;
        while (1) {
            int mi = 0;
            for (int j = 1; j <= n; j++)
                if (mark[j] && a[i][j] < a[i][mi])
                    mi = j;
            if (mi == 0) break;
            mark[mi] = false;
            for (int j = 1; j <= n; j++)
                if (mark[j] && d[mi][j] <= ee[mi] && a[i][j] > a[i][mi] + t[mi][j]) {
                    a[i][j] = a[i][mi] + t[mi][j];
                }
        }
    }

    printf("Case #%d: ", nt);

    while (q--) {
        int u, v;
        scanf("%d%d", &u, &v);
        printf("%.10f ", a[u][v]);
    }

    printf("\n");
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}
