// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-10;

const int MAX_N = (int)1e5 + 123;

int n, p;
int cnt[5];

int dp[2][105][105][105][5];

void upd(int &a, const int &b) {
    a = max(a, b);
}

int solve() {
    cin >> n >> p;
    memset(cnt, 0, sizeof cnt);
    for (int i = 1, x; i <= n; i++) {
        cin >> x;
        cnt[x % p]++;
    }
    memset(dp, -1, sizeof dp);
    dp[0][0][0][0][0] = 0;
    for (int len = 0, it = 0; len < n; len++, it ^= 1) {
        memset(dp[it ^ 1], -1, sizeof dp[it ^ 1]);
        for (int i = 0; i <= cnt[0]; i++) {
            for (int j = 0; j <= cnt[1]; j++) {
                for (int k = 0; k <= cnt[2]; k++) {
                    if (i + j + k > len)
                        break;
                    int l = len - i - j - k;
                    if (l > cnt[3])
                        continue;
                    for (int last = 0; last < p; last++) {
                        int cost = (last == 0);
                        if (i < cnt[0]) {
                            upd(dp[it ^ 1][i + 1][j][k][last], dp[it][i][j][k][last] + cost);
                        }
                        if (j < cnt[1]) {
                            upd(dp[it ^ 1][i][j + 1][k][(last + p - 1) % p], dp[it][i][j][k][last] + cost);
                        }
                        if (k < cnt[2]) {
                            upd(dp[it ^ 1][i][j][k + 1][(last + p - 2) % p], dp[it][i][j][k][last] + cost);
                        }
                        if (l < cnt[3]) {
                            upd(dp[it ^ 1][i][j][k][(last + p - 3) % p], dp[it][i][j][k][last] + cost);
                        }
                    }
                }
            }
        }
    }
    
    int ans = 0;
    for (int last = 0; last < p; last++)
        ans = max(ans, dp[n % 2][cnt[0]][cnt[1]][cnt[2]][last]);
    return ans;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int tests;
    cin >> tests;
    for (int it = 1; it <= tests; it++) {
        cout << "Case #" << it << ": " << solve() << endl;
    }
    return 0;
}
