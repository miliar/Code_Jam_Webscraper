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

int n, d[101], s[101], q;
int u[101], v[101];
LL m[101][101];
int i, j;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    for (_T = 1; _T <= T; ++_T) {
        cout << "Case #" << _T << ": ";
        cin >> n >> q;
        FOR1(i, n) {
            cin >> d[i] >> s[i];
        }
        FOR1(i, n) {
            FOR1(j, n) {
                cin >> m[i][j];
            }
        }
        FOR1(i, q) {
            cin >> u[i] >> v[i];
        }
        FOR1(i, n) {
            for(j = i+2; j <= n; ++j) {
                m[i][j] = m[i][j-1] + m[j-1][j];
            }
        }
        long double dp[101];
        dp[1] = 0;
        for( i = 2; i <= n; ++i ) {
            dp[i] = 1e18;
            FOR1(j, i-1) {
                if (d[j] >= m[j][i] && dp[j] + m[j][i] * 1.0 / s[j] < dp[i]) {
                }
                if (d[j] >= m[j][i])
                    dp[i] = min(dp[i], dp[j] + m[j][i] * 1.0 / s[j]);
            }
        }
        cout << setprecision(6) << fixed << dp[n] << endl;
    }
}