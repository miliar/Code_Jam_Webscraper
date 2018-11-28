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

LL go(LL v) {
    LL res = 1;
    while (res * 2 <= v) {
        res *= 2;
    }
    return res;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    /*REPE(n, 1, 100) {
        int st = 1;
        REPE(k, 1, n) {
            set<int> used;
            used.insert(0);
            used.insert(n + 1);

            int mx = (int) -1e9;
            int mn = (int) -1e9;

            FOR(i, k) {
                int wh = 0;
                mx = (int) -1e9;
                mn = (int) -1e9;

                set<int>::iterator it = used.begin();
                ++it;
                int l = 0;
                for (; it != used.end(); ++it) {
                    int r = *it;
                    int pos = (r + l) / 2;
                    int ls = pos - l - 1;
                    int rs = r - pos - 1;

                    int nowmn = min(ls, rs);
                    int nowmx = max(ls, rs);
                    if (nowmn > mn) {
                        mn = nowmn;
                        wh = pos;
                    }
                    if (mn == nowmn && nowmx > mx) {
                        mx = nowmx;
                        wh = pos;
                    }
                    l = r;
                }
                used.insert(wh);
            }
            if (n == 64) {
                n = 64;
            }
            int x = (n - (k - st) ) / st / 2;
            int y = (n - (k - st) ) / st / 2;
            if ((n - (k - st)) - y * 2 * st < st) {
                --y;
            }

            if (x != mx || y != mn) {
                cout << n << " " << k << " " << mx << " " << mn << "\n";
                cout << x << " " << y << "\n\n";
            }
            if (k + 1 == st * 2 || k == 1) {
                st *= 2;
            }
        }
    }*/

    int T;
    cin >> T;
    FOR(TT, T) {
        cout << "Case #" << TT + 1 << ": ";
        LL n, k;
        cin >> n >> k;
        LL st = go(k);
        LL x = (n - (k - st)) / st / 2;
        LL y = (n - (k - st)) / st / 2;
        if ((n - (k - st)) - y * 2 * st < st) {
            --y;
        }
        cout << x << " " << y << "\n";
    }
    return 0;
}