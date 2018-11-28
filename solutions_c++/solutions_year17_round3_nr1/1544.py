#include <bits/stdc++.h>
using namespace std;

const double PI =  acos(-1.0);

struct on {
        long long r, h;
        bool operator < (const on &A) const {
                return r != A.r ? r > A.r : h > A.h;
        }
}no[1010];
long long d[1010][1010];
long long p[1010];

int main () {
//        cout << PI << endl;
        freopen ("in.txt", "r", stdin);
        freopen ("out.txt", "w", stdout);
        int T;
        scanf ("%d", &T);
        for (int cas = 1; cas <= T; cas++) {
                int n, k;
                scanf ("%d%d", &n, &k);
                for (int i = 1; i <= n; i++) {
                        scanf ("%lld%lld", &no[i].r, &no[i].h);
                }
                sort (no + 1, no + n + 1);
                for (int i = 0; i <= n; i++)
                        for (int j = 0; j <= k; j++)
                                d[i][j] = 0;
                for (int i = 0; i <= k; i++)    p[i] = 0;
                for (int i = 1; i <= n; i++) {
                        for (int j = 1; j <= min (i, k); j++) {
                                if (j == 1)     d[i][j] = no[i].r * no[i].r + 2 * no[i].r * no[i].h;
                                else    d[i][j] = max (d[i][j], p[j - 1] + 2 * no[i].r * no[i].h);
                        }
                        for (int j = 1; j <= k; j++)
                                p[j] = max (p[j], d[i][j]);
                }
                long long ans = 0;
                for (int i = 1; i <= n; i++) {
                        ans = max (ans, d[i][k]);
                }
                printf ("Case #%d: %.6f\n", cas, 1.0 * PI * ans);
        }
        return 0;
}
