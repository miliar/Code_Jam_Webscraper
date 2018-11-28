#include <sys/types.h>
#include <unistd.h>
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define RFOR(i, a, b) for (int i = (b)-1; i >= int(a); --i)
#define rep(i, n) FOR(i, 0, n)
#define rep1(i, n) FOR(i, 1, int(n) + 1)
#define rrep(i, n) RFOR(i, 0, n)
#define rrep1(i, n) RFOR(i, 1, int(n) + 1)
#define all(c) begin(c), end(c)
const int MOD = 1000000007;

template <typename T>
void __dump__(std::ostream &os, const T &first) {
    os << first;
}
template <typename First, typename... Rest>
void __dump__(std::ostream &os, const First &first, const Rest &... rest) {
    os << first << ", ";
    __dump__(os, rest...);
}
#define dump(...)                                         \
    do {                                                  \
        std::ostringstream os;                            \
        os << __LINE__ << ":\t" << #__VA_ARGS__ << " = "; \
        __dump__(os, __VA_ARGS__);                        \
        std::cerr << os.str() << std::endl;               \
    } while (0)

const int INF = 1e9;

int Ac, Aj;
int C[111], D[111]; // start, end
int J[111], K[111]; // start, end

int dp[730][730][2];
bool ok[730 * 2][2];

int do_dp(int a, int b) {
    fill((int*)begin(dp), (int*)end(dp), INF);
    // rep(i, 720*2) {
    //     cout << ok[i][0];
    // }
    // cout << endl;
    // rep(i, 720*2) {
    //     cout << ok[i][1];
    // }
    // cout << endl;
    if (ok[0][0]) dp[0][0][0] = a;
    if (ok[0][1]) dp[0][0][1] = b;
    rep(t, 720 * 2 + 2) {
        rep(i, t + 1) {
            int j = t - i;
            if (i > 721 || j > 721) continue;
            if (ok[t + 1][0]) {
                dp[i + 1][j][0] = min(dp[i + 1][j][0], dp[i][j][0]);
                dp[i + 1][j][0] = min(dp[i + 1][j][0], dp[i][j][1] + 1);
            }
            if (ok[t + 1][1]) {
                dp[i][j + 1][1] = min(dp[i][j + 1][1], dp[i][j][1]);
                dp[i][j + 1][1] = min(dp[i][j + 1][1], dp[i][j][0] + 1);
            }
        }
    }
    // rep(j, 720) {
    //     cout << dp[j][0][0] << ' ';
    // }
    // cout << endl;

    // rep(i, 720) {
    //     rep(j, 720) {
    //         cout << dp[i][j][0] << "," << dp[i][j][1] << ' ';
    //     }
    //     cout << endl;
    // }

    if (a) return dp[720][720][1];
    if (b) return dp[720][720][0];
    assert(false);
    // int ans = min(dp[721][720][0], dp[720][721][1]);
    // return ans;
}

int solve() {
    memset(ok, 1, sizeof ok);
    rep(i, Ac) {
        FOR(j, C[i], D[i]) ok[j][0] = false;
    }
    ok[720*2][0] = ok[0][0];
    rep(i, Aj) {
        FOR(j, J[i], K[i]) ok[j][1] = false;
    }
    ok[720*2][1] = ok[0][1];
    int a = do_dp(1, 0);
    int b = do_dp(0, 1);
    return min(a, b);
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cin >> Ac >> Aj;
        rep(i, Ac) cin >> C[i] >> D[i];
        rep(i, Aj) cin >> J[i] >> K[i];
        int ans = solve();
        printf("Case #%d: %d\n", i + 1, ans);
    }
}
