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
    freopen("/Users/ramis/Downloads/A-large.in.txt", "rt", stdin);
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
#define INF 1000000000 //2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-12
#define N 111
/* --------- END TEMPLATE CODE --------- */
int n, p, a[N];

int solve() {
    vector<int> g(p);
    forn(i, n) g[a[i]%p] += 1;
    int res = g[0];
    if (p == 2) {
        res += (g[1] + 1) / 2;
    } else if (p == 3) {
        int y = min(g[1], g[2]);
        g[1] -= y, g[2] -= y;
        res += y;
        int x = max(g[1], g[2]);
        res += (x + 2) / 3;
    } else if (p == 4) {
        int y = min(g[1], g[3]);
        g[1] -= y, g[3] -= y;
        res += y;
        y = g[2] / 2;
        res += y;
        g[2] -= 2 * y;
        if (g[2]) {
            if (g[1] > 1) {
                res += 1;
                g[1] -= 2;
                g[2] -= 1;
            } else if (g[3] > 1) {
                res += 1;
                g[3] -= 2;
                g[2] -= 1;
            }
        }

        int rem = g[1] + g[2] + g[3];
        res += (rem + 3)/ 4;
    }
    return res;
}

void smain() {
    cin >> n;
    for (int cas = 1; cin >> n >> p; ++cas) {
        forn(i, n) cin >> a[i];

        auto res = solve();
        cout << "Case #" << cas << ": " << res << '\n';
        cerr << "Case #" << cas << ": " << res << endl;
    }
}
