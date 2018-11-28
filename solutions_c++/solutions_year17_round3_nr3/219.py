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
    os << fixed << setprecision(10);
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
const double EPS = 1e-9;

int N, K;
double U;
vector<double> p;

vector<double> assign(vector<double> ps, double lb, double u) {
    rep(i, N) {
        double give = max(0.0, lb - ps[i]);
        if (give > u + EPS) {
            return {};
        }
        ps[i] += give;
        u -= give;
        // dump(give, ps[i]);
    }
    // exit(0);
    return ps;
}

double solve() {
    if (N != K) return -1;
    double lo = 0, hi = 1.01;
    // assert(assign(p, 1.01, U).size() == 0);
    // assign(p, 1.0, U);
    rep(i, 200) {
        double mid = (lo + hi) / 2;
        auto pp = assign(p, mid, U);
        if (pp.size()) {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    // dump(lo, hi);
    auto pp = assign(p, lo, U);
    // dump(lo, hi);
    // rep(i, N) {
    //     dump(pp[i]);
    // }
    double ok = 1;
    rep(i, N) {
        ok *= pp[i];
    }
    return ok;
}

int main() {
    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    rep(i, T) {
        cin >> N >> K;
        cin >> U;
        p.resize(N);
        rep(i, N) cin >> p[i];
        double ans = solve();
        printf("Case #%d: %.10lf\n", i + 1, ans);
    }
}
