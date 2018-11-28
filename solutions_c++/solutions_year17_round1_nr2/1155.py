#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <bitset>
#include <iterator>
#include <ctime>

using namespace std;

#define FOR(i, n) for (int i=0; i<n; ++i)
#define FORE(i, n) for (int i=0; i<=n; ++i)
#define REP(i, a, b) for (int i=a; i<b; ++i)
#define REPE(i, a, b) for (int i=a; i<=b; ++i)
#define mp make_pair
#define pb push_back

typedef long double dbl;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const dbl pi = 3.14159265358979323846;
const int inf = (int) 1e9;
const dbl eps = 1e-9;

int a[5][10];
int b[10][10];

VI check(int v, int r) {
    VI res;
    int from = v / r / 1.1;
    from = max(1, from - 5);
    int to = v / r / 0.9 + 5;
    REP(j, from, to) {
        int rj = r * j;
        int z = 0;
        if (rj % 10 != 0) {
            z = 1;
        }
        if ((int)(rj * 0.9) + z <= v &&
            v <= (int)(rj * 1.1)  ) {
            res.pb(j);
        }
    }
    return res;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    FOR(TT, T) {
        cout << "Case #" << TT + 1 << ": ";
        cerr << TT << "\n";
        int n, p;
        cin >> n >> p;
        VI r(n);
        FOR(i, n) {
            cin >> r[i];
        }
        FOR(i, n) {
            FOR(j, p) {
                cin >> a[i][j];
            }
        }
        if (n == 1) {
            int res = 0;
            FOR(i, p) {
                if (!check(a[0][i], r[0]).empty()) {
                    ++res;
                }
            }
            cout << res << "\n";
            continue;
        }
        VI c(p);
        FOR(i, p) {
            c[i] = i;
        }
        int res = 0;
        do {
            int now = 0;
            FOR(i,p) {
                int x = a[0][i];
                int y = a[1][c[i]];
                VI x1 = check(x,r[0]);
                VI y1 = check(y, r[1]);
                bool ok = false;
                FOR(j,x1.size()) {
                    FOR(k,y1.size()) {
                        if (x1[j] == y1[k]) {
                            ok = true;
                            break;
                        }
                    }
                    if (ok) {
                        break;
                    }
                }
                if (ok) {
                    ++now;
                }
            }
            if (now > res) {
                res = now;
            }
            if (res == p) {
                break;
            }
        } while (next_permutation(c.begin(), c.end()));
        cout << res << "\n";
    }
    return 0;
}