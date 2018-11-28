#include <iostream>
#include <cstdio>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <fstream>
#include <memory.h>
#include <iomanip>
#include <omp.h>
#include <bitset>
#include <fstream>
#include <string>
#include <list>
#include <unordered_map>
#include <future>

using namespace std;

#define right asfdsg
#define left asfdsvs
#define pb emplace_back
#define F first
#define S second
#define mp make_pair
#define x1 _xxx1
#define y1 _yyy1

#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef std::pair < int, int > pii;
typedef std::pair < ll, ll > pll;
typedef std::vector < std::vector < ld > > vld;

const int INF = (int) 2e9 + 7;
const ld EPS = (ld) 1e-5;
const int BASE = (int) 1e9 + 7;
const int MAXN = 1111;
const ll INFLL = (ll) 1e18;
const ld PI = acos(-1);

int n, k;
int h[MAXN], r[MAXN];
int p[MAXN];
ll f[2][MAXN];

void upd(ll &x, ll y) {
    if (x == -1) x = y;
    else if (y != -1) x = max (x, y);
}

ld solve() {
    scanf ("%d%d", &n, &k);
    for (int i = 1; i <= n; i ++)
        scanf ("%d%d", &r[i], &h[i]);
    for (int i= 1; i <= n; i ++) p[i] = i;
    sort (p + 1, p + 1 + n, [](int i, int j) { return r[i] > r[j]; } );
    memset (f, -1, sizeof(f));
    f[0][0] = 0;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j <= k; j ++) {
            if (f[i&1][j] == -1) continue;
            int rr = r[ p[i + 1] ], hh = h[ p[i + 1] ];
            upd(f[(i + 1)&1][j], f[i&1][j]);
            if (j) upd(f[(i + 1) & 1][j + 1], f[i&1][j] + 2ll * rr * hh);
            else upd (f[(i + 1)&1][j + 1], f[i&1][j] + 2ll * rr * hh + 1ll * rr * rr);
        }
        memset(f[i&1], -1, sizeof(f[i&1]));
    }
    return 1.L * PI * f[n&1][k];
}

int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i ++) {
        cout << "Case #" << i << ": ";
        cout << fixed << setprecision(8) << solve() << "\n";
    }
    return 0;
}
