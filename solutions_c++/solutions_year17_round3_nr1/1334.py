#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define FI first
#define SE second
#define pb push_back
#define mp make_pair

typedef long long LL;

int T, _T;

struct p {
    LL r, h;
    p(){}
    p(LL r, LL h) : r(r), h(h) {}
};

bool operator < (p p1, p p2) {
    return p1.r > p2.r;
}

p pk[1001];
int n, k, i, j;
LL dp[1001][1001];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    for (_T = 1; _T <= T; ++_T) {
        cout << "Case #" << _T << ": ";
        cin >> n >> k;
        FOR1(i, n) {
            cin >> pk[i].r >> pk[i].h;
        }
        sort(pk + 1, pk + n + 1);
        FOR1(i, n) {
            FOR1(j, n) {
                dp[i][j] = 0;
            }
        }
        FOR1(i, n) {
            dp[i][1] = max(dp[i-1][1], pk[i].r * pk[i].r + 2 * pk[i].r * pk[i].h);
            for ( j = 2; j <= k; ++j ) {
                dp[i][j] = dp[i-1][j];
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 2 * pk[i].r * pk[i].h);
            }
        }
        cout << setprecision(8) << fixed << M_PI * dp[n][k] << endl;
    }
}