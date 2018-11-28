#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <tuple>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

int a[6], l[6], r[6];
bool g[6][6];
int n;

int main() {
//    freopen("B-small-attempt1.in", "rt", stdin);
    freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    char name[7] = "ROYGBV";
    int t;
    cin >> t;
    forn (q, t) {
        cerr << q + 1 << endl;
        cout << "Case #" << q + 1 << ": ";
        cin >> n;
        forn (i, 6) {
            cin >> a[i];
        }
        bool ok = true;
        bool was = false;
        for (int i = 0; i < 6; i += 2) {
            if (a[i] + a[(i + 3) % 6] < n) {
                continue;
            }
            if (a[i] != a[(i + 3) % 6]) {
                ok = false;
                break;
            }
            was = true;
            forn (j, n / 2) {
                cout << name[i] << name[(i + 3) % 6];
            }
            cout << endl;
        }
        if (was) {
            continue;
        }
        for (int i = 0; i < 6; i += 2) {
            if (a[(i + 3) % 6] && a[i] <= a[(i + 3) % 6]) {
                ok = false;
                break;
            }
        }
        if (!ok) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        for (int i = 0; i < 6; i += 2) {
            a[i] -= a[(i + 3) % 6];
        }
        n = a[0] + a[2] + a[4];
        int mx = 0;
        bool was_c[6];
        forn (i, 6) {
            was_c[i] = false;
        }
        if (a[2] > a[mx]) {
            mx = 2;
        }
        if (a[4] > a[mx]) {
            mx = 4;
        }
        int x1 = 0, x2 = 2;
        if (mx == 0) {
            x1 = 4;
        }
        if (mx == 2) {
            x2 = 4;
        }
        if (a[mx] * 2 > n) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            forn (i, a[mx]) {
                cout << name[mx];
                if (!was_c[mx]) {
                    was_c[mx] = true;
                    forn (i, a[(mx + 3) % 6]) {
                        cout << name[(mx + 3) % 6] << name[mx];
                    }
                }
                if (a[x1] >= a[x2]) {
                    cout << name[x1];
                    --a[x1];
                    if (!was_c[x1]) {
                        was_c[x1] = true;
                        forn (i, a[(x1 + 3) % 6]) {
                            cout << name[(x1 + 3) % 6] << name[x1];
                        }
                    }
                } else {
                    cout << name[x2];
                    --a[x2];
                    if (!was_c[x2]) {
                        was_c[x2] = true;
                        forn (i, a[(x2 + 3) % 6]) {
                            cout << name[(x2 + 3) % 6] << name[x2];
                        }
                    }
                }
            }
            forn (i, n - a[mx] * 2) {
                if (a[x1] >= a[x2]) {
                    cout << name[x1];
                    --a[x1];
                    if (!was_c[x1]) {
                        was_c[x1] = true;
                        forn (i, a[(x1 + 3) % 6]) {
                            cout << name[(x1 + 3) % 6] << name[x1];
                        }
                    }
                } else {
                    cout << name[x2];
                    --a[x2];
                    if (!was_c[x2]) {
                        was_c[x2] = true;
                        forn (i, a[(x2 + 3) % 6]) {
                            cout << name[(x2 + 3) % 6] << name[x2];
                        }
                    }
                }
            }
            cout << endl;
        }
    }
}
