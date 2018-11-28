#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int MAXN = int(2e5) + 200;
const int INF = int(1e9) + 10;
const long long LINF = 1LL * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test;
int n, p, ans;
int dp[103][103][103][4];
int cnt[4];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> test;
    for (int iter = 1; iter <= test; iter++) {
        clr(dp, -1);
        clr(cnt, 0);
        cin >> n >> p;
        ans = 0;
        for (int i = 0; i < n; i++) {
            int g;
            cin >> g;
            if (g % p == 0) {
                ans++;
            } else {
                cnt[g % p]++;
            }
        }

        dp[cnt[1]][cnt[2]][cnt[3]][0] = 0;
        for (int r1 = cnt[1]; r1 >= 0; r1--) {
            for (int r2 = cnt[2]; r2 >= 0; r2--) {
                for (int r3 = cnt[3]; r3 >= 0; r3--) {
                    for (int rem = 0; rem < p; rem++) {
                        if (dp[r1][r2][r3][rem] >= 0) {
                            int add = (rem == 0);
                            if (r1 > 0) {
                                dp[r1 - 1][r2][r3][(rem - 1 + p) % p] = max(dp[r1 - 1][r2][r3][(rem - 1 + p) % p], dp[r1][r2][r3][rem] + add);
                            }

                            if (r2 > 0) {
                                dp[r1][r2 - 1][r3][(rem - 2 + p) % p] = max(dp[r1][r2 - 1][r3][(rem - 2 + p) % p], dp[r1][r2][r3][rem] + add);
                            }

                            if (r3 > 0) {
                                dp[r1][r2][r3 - 1][(rem - 3 + p) % p] = max(dp[r1][r2][r3 - 1][(rem - 3 + p) % p], dp[r1][r2][r3][rem] + add);
                            }
                        }
                    }
                }
            }
        }

        int total = 0;
        for (int rem = 0; rem < p; rem++) {
            total = max(total, dp[0][0][0][rem]);
        }
        ans += total;
        cout << "Case #" << iter << ": " << ans << endl;
    }
    return 0;
}
