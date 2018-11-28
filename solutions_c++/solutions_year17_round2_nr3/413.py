#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int MAXN = 101;
const double INF = 1e14;

int n, q;
double e[MAXN], s[MAXN];
double m[MAXN][MAXN];
double g[MAXN][MAXN];

int main()
{
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%d %d", &n, &q);

        for (int i = 1; i <= n; i++) {
            scanf("%lf %lf", &e[i], &s[i]);
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                scanf("%lf", &m[i][j]);
                if (m[i][j] < 0) m[i][j] = INF;
            }
        }

        for (int k = 1; k <= n; k++)
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++)
                    m[i][j] = min(m[i][j], m[i][k] + m[k][j]);

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j) g[i][j] = INF;
                else if (m[i][j] > e[i]) g[i][j] = INF;
                else g[i][j] = m[i][j]/s[i];
            }
        }

        for (int k = 1; k <= n; k++)
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++)
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]);

        int a, b;
        printf("Case #%d:", t);
        while (q--) {
            scanf("%d %d", &a, &b);
            printf(" %lf", g[a][b]);
        }
        printf("\n");
    }
}
