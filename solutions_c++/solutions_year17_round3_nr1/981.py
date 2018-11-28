/**

**/
#include <bits/stdc++.h>
using namespace std;

#define N 200005
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, r[N], h[N], k, a[N], kt[N], b[2000][2000];
double kq;

void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> n >> k;
        for (int i = 1; i <= n; i++) cin >> r[i] >> h[i];
        for (int i = 1; i <= n; i++) a[i] = 2 * r[i] * h[i];
        for (int i = 1; i <= n; i++) {
            int l = i;
            for (int j = i + 1; j <= n; j++)
                if (r[j] > r[l] || (r[j] == r[l] && h[j] > h[l])) l = j;
            swap(r[i], r[l]);
            swap(h[i], h[l]);
            swap(a[i], a[l]);
        }
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) b[i][j] = 0;
        for (int i = 1; i <= n; i++) b[i][1] = r[i] * r[i] + a[i];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j < i; j++)
                for (int l = 2; l <= k; l++)
                    if (b[j][l - 1] == 0) break;
                    else
                        b[i][l] = max(b[i][l], b[j][l - 1] + a[i]);
        long long kqq = 0;
        for (int i = 1; i <= n; i++) kqq = max(kqq, b[i][k]);
        kq = double(kqq) * PI;
        printf("Case #%d: %.9f\n", te, kq);
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
