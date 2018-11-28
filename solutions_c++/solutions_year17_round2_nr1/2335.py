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

string solve(const string &s) {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    int ans = 0;
    rep(i, 100000000) ans ^= i;
    dump(s);
    return s + s + to_string(ans);
}

int N, D;
vector<int> K, S;

double solve() {
    double maxi = 0;
    rep(i, N) {
        double d = D - K[i];
        double t = d / S[i];
        maxi = max(maxi, t);
    }
    return D / maxi;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cin >> D >> N;
        K.resize(N);
        S.resize(N);
        rep(i, N) cin >> K[i] >> S[i];
        double ans = solve();
        printf("Case #%d: %.10lf\n", i + 1, ans);
    }
}
