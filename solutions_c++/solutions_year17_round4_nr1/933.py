#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <deque>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <complex>
#include <cstring>
#include <cassert>
#include <bitset>

using namespace std;
#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define repd(i, a, b) for(int i = (a); i > (b); i--)
#define forIt(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define forRev(it, a) for(__typeof((a).rbegin()) it = (a).rbegin(); it != (a).rend(); it++)
#define ft(a) __typeof((a).begin())
#define ll long long
#define ld long double
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define bitcount(n) __builtin_popcountll(n)

typedef complex<ld> cplex;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;

const int N = 100 + 7;
const int M = 20;
const int inf = 1000000007;
const long long linf = 1e18 + 7;
const double pi = acos(-1);
const double eps = 1e-9;
const bool multipleTest = 1;

int n, p;
int cnt[10];

int dp[2][N][N][N][4];

void calc2() {
    cnt[0] = cnt[1] = 0;
    for(int i = 0; i < n; ++i) {
        int u; scanf("%d", &u);
        cnt[u & 1] ++;
    }

    cout << cnt[0] + (cnt[1] + 1) / 2 << '\n';
}

void calc3() {
    for (int j = 0; j < p; ++j) cnt[j] = 0;
    for(int i = 0; i < n; ++i) {
        int u;
        scanf("%d", &u);
        cnt[u % p]++;
    }

    int cur = 0;
    rep(i, 0, cnt[0] + 1)
        rep(j, 0, cnt[1] + 1)
            rep(t, 0, cnt[2] + 1) {
                rep(k, 0, p) dp[cur][i][j][t][k] = -inf;
            }
    dp[cur][0][0][0][0] = 0;

    for (int xx = 1; xx <= n; ++xx) {
        int pre = cur;
        cur ^= 1;
        rep(i, 0, cnt[0] + 1)
            rep(j, 0, cnt[1] + 1)
                rep(t, 0, cnt[2] + 1) {
                    rep(k, 0, p) {
                        int& res = dp[cur][i][j][t][k];
                        res = -inf;
                        if (i > 0) {
                            res = max(res, dp[pre][i - 1][j][t][k] + (k == 0));
                        }
                        if (j > 0) {
                            res = max(res, dp[pre][i][j - 1][t][(k + 1) % p] + (k == p - 1));
                        }
                        if (t > 0) {
                            res = max(res, dp[pre][i][j][t - 1][(k + 2) % p] + (k == p - 2));
                        }
                    }
                }
    }

    int ans = -inf;
    for (int k = 0; k < p; ++k)
        ans = max(ans, dp[cur][cnt[0]][cnt[1]][cnt[2]][k]);
    cout << ans << '\n';
}

void calc4(){
    for (int j = 0; j < p; ++j) cnt[j] = 0;
    for(int i = 0; i < n; ++i) {
        int u;
        scanf("%d", &u);
        cnt[u % p]++;
    }

    int cur = 0;
    rep(i, 0, cnt[0] + 1)
        rep(j, 0, cnt[1] + 1)
            rep(t, 0, cnt[2] + 1) {
                rep(k, 0, p) dp[cur][i][j][t][k] = -inf;
            }
    dp[cur][0][0][0][0] = 0;

    for (int xx = 1; xx <= n; ++xx) {
        int pre = cur;
        cur ^= 1;
        rep(i, 0, cnt[0] + 1)
            rep(j, 0, cnt[1] + 1)
                rep(t, 0, cnt[2] + 1) {
                    rep(k, 0, p) {
                        int& res = dp[cur][i][j][t][k];
                        res = -inf;
                        if (i > 0) {
                            res = max(res, dp[pre][i - 1][j][t][k] + (k == 0));
                        }
                        if (j > 0) {
                            res = max(res, dp[pre][i][j - 1][t][(k + 1) % p] + (k == p - 1));
                        }
                        if (t > 0) {
                            res = max(res, dp[pre][i][j][t - 1][(k + 2) % p] + (k == p - 2));
                        }
                        int r = xx - i - j - t;
                        if (r > 0) {
                            res = max(res, dp[pre][i][j][t][(k + 3) % p] + (k == p - 3));
                        }
                    }
                }
    }

    int ans = -inf;
    for (int k = 0; k < p; ++k)
        ans = max(ans, dp[cur][cnt[0]][cnt[1]][cnt[2]][k]);
    cout << ans << '\n';
}

void solve() {

    cin >> n >> p;
    if (p == 2) {
        calc2();
    } else {
        if (p == 3) calc3();
        else calc4();
    }





}

int main() {
#ifdef _LOCAL_
    freopen("in.txt", "r", stdin);
#endif
        freopen("out.txt", "w", stdout);
    int Test = 1;
    if (multipleTest) {
        cin >> Test;
    }
    for(int i = 0; i < Test; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
#ifdef _LOCAL_
//    cout<<"\n" << 1.0 * clock() / CLOCKS_PER_SEC;
#endif
}


// fu = fk + ck^2 * (k - u + 1)  + cu * (n - k ... n - u) - hk
// - ck^2 * u - ck (1 .. u)
// - 2cu * n * u + cu * u * (u - 2) = ck * [u * (u - 2 - 2 * n)] + g(x)
