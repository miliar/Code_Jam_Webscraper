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

const int n = 24 * 60;
int c[n + 10];
int d[n + 10][n / 2 + 10][2][2];

int main() {
//    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        cout << "Case #" << q + 1 << ": ";
        forn (i, n) {
            c[i] = 2;
        }
        int a, b;
        cin >> a >> b;
        forn (i, a) {
            int x, y;
            cin >> x >> y;
            for (int j = x; j < y; ++j) {
                c[j] = 0;
            }
        }
        forn (i, b) {
            int x, y;
            cin >> x >> y;
            for (int j = x; j < y; ++j) {
                c[j] = 1;
            }
        }
        forn (i, n + 1) {
            forn (j, n / 2 + 1) {
                forn (k, 2) {
                    forn (l, 2) {
                        d[i][j][k][l] = 2000000000;
                    }
                }
            }
        }
        if (c[0] != 1) {
            d[1][1][0][0] = 0;
        }
        if (c[0] != 0) {
            d[1][0][1][1] = 0;
        }
        for (int i = 1; i < n; ++i) {
            forn (j, n / 2 + 1) {
                forn (k, 2) {
                    forn (l, 2) {
                        if (c[i] != 1) {
                            d[i + 1][j + 1][k][0] = min(d[i + 1][j + 1][k][0], d[i][j][k][l] + (l == 1));
                        }
                        if (c[i] != 0) {
                            d[i + 1][j][k][1] = min(d[i + 1][j][k][1], d[i][j][k][l] + (l == 0));
                        }
                    }
                }
            }
//            cerr << c[i];
        }
//        cerr << endl;
        int ans = 2000000000;
        forn (k, 2) {
            forn (l, 2) {
                ans = min(ans, d[n][n / 2][k][l] + (k != l));
            }
        }
        cout << ans << endl;
    }
}
