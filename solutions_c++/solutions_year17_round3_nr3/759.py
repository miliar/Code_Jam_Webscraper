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


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    FOR(TT, T) {
        cout << "Case #" << TT + 1 << ": ";
        cerr << TT + 1 << "\n";
        int n, k;
        cin >> n >> k;
        vector<dbl> d(n);
        dbl u;
        cin >> u;
        dbl sum = u;
        FOR(i, n) {
            cin >> d[i];
            sum += d[i];
        }
        if (sum >= n) {
            cout << fixed << setprecision(9) << 1.0 << "\n";
            continue;
        }
        sort(d.begin(), d.end());
        int i = 0;
        while (i < n && u >= 0) {
            while (i < n && d[i] == d[0]) {
                ++i;
            }
            if (i < n) {
                dbl nxt = d[i];
                nxt -= d[0];
                if (u >= nxt * i) {
                    FOR(j, i) {
                        d[j] += nxt;
                    }
                    u -= nxt * i;
                } else {
                    FOR(j, i) {
                        d[j] += min(u / i, (dbl)1.0);
                    }
                    break;
                }
            } else {
                FOR(j, n) {
                    d[j] += min(u / n, (dbl)1.0);
                }
            }
        }
        dbl res = 1;
        FOR(j, n) {
            res *= d[j];
        }
        res = min(res, (dbl)1.0);
        cout << fixed << setprecision(9) << res << "\n";
    }
    return 0;
}