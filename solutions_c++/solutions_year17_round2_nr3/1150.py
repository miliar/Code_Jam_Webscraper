/**

**/
#include <bits/stdc++.h>
using namespace std;
#define N 2002
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, q, a[N][N], e[N], s[N], u, v, d[N][N];
double kq;
void duyet(int u, int k, int l, double ans) {
    //cout << u << " " << v << " " << ans << endl;
    if (u == v) {
        if (kq > ans) kq = ans;
        return;
    }
    for (int i = u + 1; i <= u + 1; i++)
        if (a[u][i] > -1) {
            if (k - a[u][i] >= 0) {
                if (k - a[u][i] > e[i] || l > s[i]) duyet(i, k - a[u][i], l, ans + double(a[u][i]) / double(l));
                if (k - a[u][i] < e[i] || l < s[i]) duyet(i, e[i], s[i], ans + double(a[u][i]) / double(l));
            }
        }
}
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> n >> q;
        for (int i = 1; i <= n; i++) cin >> e[i] >> s[i];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) cin >> a[i][j];
        for (int i = 1; i <= q; i++) {
            cin >> u >> v;
        }
        kq = 100000000000000;
        duyet(u, e[u], s[u], 0);
        cout << "Case #" << te << ": ";
        printf("%.6f\n", kq);
    }
}
int main() {
    freopen("main.in", "r", stdin);
    //freopen("main.in", "w", stdout);
    freopen("main.out", "w", stdout);
    solve();
    //fclose(stdin);
    //fclose(stdout);
}
///CTKB1997
