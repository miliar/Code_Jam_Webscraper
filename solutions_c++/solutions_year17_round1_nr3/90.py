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
    freopen("/Users/ramis/Downloads/C-small-attempt1.in.txt","rt",stdin);
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
//#define int long long
#define mp(a,b) make_pair(a,b)
#define INF 1000000000 //2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-8
#define N 111
/* --------- END TEMPLATE CODE --------- */

int Hd, Ad, Hk, Ak, B, D;
int d[N][N][N][N];

int solve(int i, int j, int k, int l) {
    if (i <= 0) return 0;
    if (j <= 0) return INF;
    if (d[i][j][k][l] != -1) return d[i][j][k][l];
    d[i][j][k][l] = INF;
    if (i - k <= 0 || j > l) d[i][j][k][l] = min(d[i][j][k][l], 1 + solve(i - k, j - l, k, l));
    if (j > l && B > 0) d[i][j][k][l] = min(d[i][j][k][l], 1 + solve(i, j - l, min(N - 1, k + B), l)); 
    if (j > max(0, l - D) && D > 0) d[i][j][k][l] = min(d[i][j][k][l], 1 + solve(i, j - max(0, l - D), k, max(0, l - D))); 
    if (j != Hd) d[i][j][k][l] = min(d[i][j][k][l], 1 + solve(i, Hd - l, k, l));
    return d[i][j][k][l];
}

void smain() {
    int n;
    cin >> n;
    for (int cas = 1; cin >> Hd >> Ad >> Hk >> Ak >> B >> D; ++cas) {
        memset(d, 255, sizeof(d));
        int res = solve(Hk, Hd, Ad, Ak);

        cout << "Case #" << cas << ": " << (res == INF ? "IMPOSSIBLE" : to_string(res)) << "\n";
        cerr << "Case #" << cas << ": " << (res == INF ? "IMPOSSIBLE" : to_string(res)) << endl;
    }
}

