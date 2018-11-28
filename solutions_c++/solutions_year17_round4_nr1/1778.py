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
int n, p;
int g[101];

int solve() {
    rep(i, n) g[i] %= p;
    if (p == 3) {
        int A = count(g, g + n, 0);
        int B = count(g, g + n, 1);
        int C = count(g, g + n, 2);
        static int dp[101][101][101];
        fill((int*)begin(dp), (int*)end(dp), INF);
        dp[0][0][0] = 0;
        rep(a, A + 1) rep(b, B + 1) rep(c, C + 1) {
            int sum = (a*0 + b*1 + c*2) % p;
            int add = sum == 0 ? 0 : 1;
            dp[a+1][b][c] = min(dp[a+1][b][c], dp[a][b][c] + add);
            dp[a][b+1][c] = min(dp[a][b+1][c], dp[a][b][c] + add);
            dp[a][b][c+1] = min(dp[a][b][c+1], dp[a][b][c] + add);
        }
        return n - dp[A][B][C];
    } else if (p == 2) {
        int A = count(g, g + n, 0);
        int B = count(g, g + n, 1);
        static int dp[101][101];
        fill((int*)begin(dp), (int*)end(dp), INF);
        dp[0][0] = 0;
        rep(a, A + 1) rep(b, B + 1) {
            int sum = (a*0 + b*1) % p;
            int add = sum == 0 ? 0 : 1;
            dp[a+1][b] = min(dp[a+1][b], dp[a][b] + add);
            dp[a][b+1] = min(dp[a][b+1], dp[a][b] + add);
        }
        return n - dp[A][B];
    } else {
        return -1;
    }
}

int main() {
    int T;
    cin >> T;
    rep(it, T) {
        cin >> n >> p;
        rep(i, n) cin >> g[i];
        int ans = solve();
        printf("Case #%d: %d\n", it + 1, ans);
    }
}
