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

int K, N;
double R[1010];
double H[1010];

const double PI = acos(-1);

double solve() {
    double ans = 0;
    rep(i, N) {
        vector<double> yoko;
        rep(j, N) {
            if (i == j) continue;
            if (R[i] < R[j]) continue;
            yoko.push_back(R[j] * H[j] * 2);
        }
        if ((int)yoko.size() < K - 1) continue;
        sort(all(yoko));
        reverse(all(yoko));
        double cand = 0;
        cand += R[i] * H[i] * 2;
        rep(j, K - 1) {
            cand += yoko[j];
        }
        cand += R[i]*R[i];
        ans = max(ans, cand);
    }
    return ans * PI;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cin >> N >> K;
        rep(i, N) cin >> R[i] >> H[i];
        double ans = solve();
        printf("Case #%d: %.10lf\n", i + 1, ans);
    }
}
