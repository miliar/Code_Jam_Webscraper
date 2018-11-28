/**

**/
#include <bits/stdc++.h>
using namespace std;

#define N 200005
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, k, m;
long long a[N], b[N], c[N], d[N], kq;
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> m >> n;
        for (int i = 1; i <= m; i++) cin >> a[i] >> b[i];
        for (int i = 1; i <= n; i++) cin >> c[i] >> d[i];
        if (m + n == 1) {
            kq = 2;
        } else {
            if (m == 2 || n == 2) {
                if (m == 2) {
                    if (a[1] > a[2]) {
                        swap(a[1], a[2]);
                        swap(b[1], b[2]);
                    }
                    int k = b[2] - a[1];
                    if (b[1] + 1440 - a[2] < k) k = b[1] + 1440 - a[2];
                    if (k <= 720) kq = 2; else kq = 4;
                    if (kq == 4 && a[2] - b[1] >= 720) kq = 2;
                } else {
                    if (c[1] > c[2]) {
                        swap(c[1], c[2]);
                        swap(d[1], d[2]);
                    }
                    int k = d[2] - c[1];
                    if (d[1] + 1440 - c[2] < k) k = d[1] + 1440 - c[2];
                    if (k <= 720) kq = 2; else kq = 4;
                    if (kq == 4 && c[2] - d[1] >= 720) kq = 2;
                }
            }
            else kq = 2;
        }
        printf("Case #%d: %d\n", te, kq);
        //cout << m << " " << n << endl;
        //for (int i = 1; i <= m; i++) cout << a[i] << " " << b[i] << endl;
        //for (int i = 1; i <= n; i++) cout << c[i] << " " << d[i] << endl;
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
