#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define N 100

ll e[N], s[N];
ll d[N][N];
double t[N][N];

void minimize(ll &a, const ll &b) {
    if (a > b && b != -1)
        a = b;
}

void solve() {
    int n, q;
    scanf("%d%d", &n, &q);
    for (int i = 0; i < n; ++i) {
        scanf("%lld%lld", &e[i], &s[i]);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%lld", &d[i][j]);
        }
        d[i][i] = 0;
    }
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            if (d[i][k] == -1)
                continue;
            for (int j = 0; j < n; ++j) {
                if (d[k][j] == -1)
                    continue;
                ll alt = d[i][k] + d[k][j];
                if (d[i][j] > alt || d[i][j] == -1)
                    d[i][j] = alt;
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (e[i] < d[i][j] || d[i][j] == -1)
                t[i][j] = std::numeric_limits<double>::infinity();
            else
                t[i][j] = double(d[i][j]) / double(s[i]);
        }
    }
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                double alt = t[i][k] + t[k][j];
                if (t[i][j] > alt)
                    t[i][j] = alt;
            }
        }
    }
    for (int i = 0; i < q; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        --u, --v;
        printf(" %.20lf", t[u][v]);
    }
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d:", i + 1);
        solve();
        putchar('\n');
    }
}
