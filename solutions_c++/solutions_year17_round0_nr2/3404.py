#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int maxN = 1010;

#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define ll long long

ll f[20][10][2], res, n, POW[20];
int test, c[20];

int digit(ll x) {
    int tmp = 0;
    while (x) tmp++, x /= 10;
    return tmp;
}

ll dp(int i, int j, bool ok) {
    if (f[i][j][ok] != -1) return f[i][j][ok];
    if (i > c[0]) return 0;
    ll tmp = 0;
    int cmax = 9;
    if (!ok) cmax = c[i];
    foru(p, j, cmax) {
        bool nok = (ok || (p < c[i]));
        ll val = dp(i + 1, p, nok);
        ll nval = (i != c[0]) ? POW[digit(val)] * p + val : p;
        tmp = max(tmp, nval);
    }
    f[i][j][ok] = tmp;
    return tmp;
}

int main() {
    POW[0] = 1;
    foru(i, 1, 18) POW[i] = POW[i - 1] * 10;
    cin >> test;
    foru(t, 1, test) {
        cin >> n; c[0] = 0;
        while (n)  c[++c[0]] = n % 10, n /= 10;
        reverse(c + 1, c + c[0] + 1);
        memset(f, 255, sizeof(f));
        res = dp(1, 0, false);
        cout << "Case #" << t << ": " << res << endl;
    }
}
