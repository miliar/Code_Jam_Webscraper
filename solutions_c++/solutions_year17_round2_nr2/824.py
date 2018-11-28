#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 2017;

int tc, n, r, o, y, g, b, v;
bool bflag = 0;
bool yflag = 0;
bool rflag = 0;

void check(char c) {
    if (c == 'B' && !bflag) {
        bflag = 1;
        for (int i = 0; i < o; i++) {
            cout << "OB";
        }
    } else if (c == 'Y' && !yflag) {
        yflag = 1;
        for (int i = 0; i < v; i++) {
            cout << "VY";
        }
    } else if (c == 'R' && !rflag) {
        rflag = 1;
        for (int i = 0; i < g; i++) {
            cout << "GR";
        }
    }
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> r >> o >> y >> g >> b >> v;
        if (o > b || v > y || g > r) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        if ((o == b && o + b != n && o + b != 0) || (v == y && v + y != n && v + y != 0) || (g == r && g + r != n && g + r != 0)) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        b -= o;
        y -= v;
        r -= g;
        int mx, mn1, mn2;
        char mxc, mnc1, mnc2;
        if (r >= y && r >= b) {
            mx = r;
            mn1 = y;
            mn2 = b;
            mxc = 'R';
            mnc1 = 'Y';
            mnc2 = 'B';
        } else if (y >= r && y >= b) {
            mx = y;
            mn1 = r;
            mn2 = b;
            mxc = 'Y';
            mnc1 = 'R';
            mnc2 = 'B';
        } else {
            mx = b;
            mn1 = r;
            mn2 = y;
            mxc = 'B';
            mnc1 = 'R';
            mnc2 = 'Y';
        }
        if (mn1 + mn2 < mx) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        bflag = 0;
        rflag = 0;
        yflag = 0;
        int cnt = mn1 + mn2 - mx;
        for (int i = 0; i < mx; i++) {
            cout << mxc;
            check(mxc);
            if (i < cnt) {
                cout << mnc1;
                check(mnc1);
                cout << mnc2;
                check(mnc2);
                mn1--;
                mn2--;
            } else {
                if (mn1) {
                    cout << mnc1;
                    check(mnc1);
                    mn1--;
                } else {
                    cout << mnc2;
                    check(mnc2);
                    mn2--;
                }
            }
        }
        if (!bflag && o) {
            check('B');
        }
        if (!yflag && v) {
            check('Y');
        }
        if (!rflag && g) {
            check('R');
        }
        cout << "\n";
    }
}
