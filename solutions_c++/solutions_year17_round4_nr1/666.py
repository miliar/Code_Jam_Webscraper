/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

int t, n, p, g[101];
int cnt[4];
int dp[2][4][101][101][101];

void solve() {
    scanf("%d%d", &n, &p);
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < n; ++i) {
        scanf("%d", &g[i]);
        cnt[g[i] % p]++;
    }
    // for (int i = 0; i < p; ++i) output(cnt[i]);
    memset(dp, 0, sizeof(dp));
    dp[0][0][cnt[1]][cnt[2]][cnt[3]] = 0;
    int m = cnt[1] + cnt[2] + cnt[3];
    for (int i = 0; i < m; ++i) {
        // output(i);
        memset(dp[(i + 1) & 1], 0, sizeof(dp[(i + 1) & 1]));
        for (int mod = 0; mod < p; ++mod) {
            for (int a = 0; a <= cnt[1]; ++a) {
                for (int b = 0; b <= cnt[2]; ++b) {
                    for (int c = 0; c <= cnt[3]; ++c) {
                        // printf("-- %d %d %d %d %d\n", i, mod, a, b, c);
                        if (a > 0) {
                            int &r = dp[(i + 1) & 1][(mod + 1) % p][a - 1][b][c];
                            r = max(r, dp[i & 1][mod][a][b][c] + (mod == 0 ? 1 : 0));
                        }
                        if (b > 0) {
                            int &r = dp[(i + 1) & 1][(mod + 2) % p][a][b - 1][c];
                            r = max(r, dp[i & 1][mod][a][b][c] + (mod == 0 ? 1 : 0));
                        }
                        if (c > 0) {
                            int &r = dp[(i + 1) & 1][(mod + 3) % p][a][b][c - 1];
                            r = max(r, dp[i & 1][mod][a][b][c] + (mod == 0 ? 1 : 0));
                        }
                    }
                }
            }
        }
    }
    // puts("ok");
    int k = 0;
    for (int i = 0; i < p; ++i)
        k = max(k, dp[m & 1][i][0][0][0]);
    printf("Case #%d: %d\n", ++t, cnt[0] + k);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
