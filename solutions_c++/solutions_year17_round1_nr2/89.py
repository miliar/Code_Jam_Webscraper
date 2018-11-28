#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>
#include <stdlib.h>
using namespace std;

void smain();
int main() {
    ios_base::sync_with_stdio(0);
#ifdef TASK
    //freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/B-large.in.txt","rt",stdin);
    freopen(TASK".out","wt",stdout);
    const clock_t start = clock();
#endif
    smain();
#ifdef TASK
    cerr << "\nTotal Execution Time: " << float( clock () - start ) /  CLOCKS_PER_SEC << endl;
#endif
    return 0;
}

#ifndef M_PI
#define M_PI 3.14159265358979311599796346854418516
#endif
#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define LL long long
#define int long long
#define mp(a,b) make_pair(a,b)
#define INF 2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-8
#define N 55
/* --------- END TEMPLATE CODE --------- */
int a[N][N];
int r[N], p[N];
bool used[N][N];


void smain() {
    int n, m;
    cin >> n;
    for (int cas = 1; cin >> n >> m; ++cas) {
        forn(i, n) cin >> r[i];
        forn(i, n) forn(j, m) cin >> a[i][j];
        forn(i, n) sort(a[i], a[i] + m);
        memset(used, 0, sizeof(used));
        int mx = 0, res = 0;
        forn(i, m) mx = max(mx, (int)(a[0][i] / 0.9 + 1));
        cerr << mx << endl;
        for (int w = 1; w <= mx; ++w) {
            while (1) {
                bool ok = 1;
                forn(i, n) {
                    double lo = w * r[i] * 0.9, hi = w * r[i] * 1.1;
                    int j = 0;
                    for (; j < m; ++j) if (!used[i][j] && a[i][j] >= lo && a[i][j] <= hi) break;
                    if (j == m) { ok = 0; break; }
                    p[i] = j;
                }
                if (ok) {
                    forn(i, n) used[i][p[i]] = 1;
                    res += 1;
                } else {
                    break;
                }
            }
        }
        cout << "Case #" << cas << ": " << res << "\n";
        cerr << "Case #" << cas << ": " << res << endl;
    }
}

