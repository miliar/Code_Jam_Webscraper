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
    freopen("/Users/ramis/Downloads/A-large.in.txt","rt",stdin);
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
char a[N][N];

void smain() {
    int n, m;
    cin >> n;
    for (int cas = 1; cin >> n >> m; ++cas) {
        forn(i, n) cin >> a[i];
        forn(i, n) {
            char pr = '?';
            forn(j, m) {
                if (a[i][j] == '?') a[i][j] = pr;
                pr = a[i][j];
            }
            pr = '?';
            rforn(j, m) {
                if (a[i][j] == '?') a[i][j] = pr;
                pr = a[i][j];
            }
        }
        forn(_t, n) forn(i, n) {
            if (a[i][0] != '?') continue;
            int p = -1;
            if (i && a[i-1][0] != '?') p = i - 1;
            else if (i < n - 1 && a[i+1][0] != '?') p = i + 1;
            if (p == -1) continue;
            forn(j, m) a[i][j] = a[p][j];
        }
        cout << "Case #" << cas << ":\n";
        forn(i, n) { forn(j, m) cout << a[i][j]; cout << '\n'; }
        cerr << "Case #" << cas << ":\n";
        forn(i, n) { forn(j, m) cerr << a[i][j]; cerr << '\n'; }
    }
}

