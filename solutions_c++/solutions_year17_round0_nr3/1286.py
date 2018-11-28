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

using pll = pair<ll,ll>;

struct Solver {
    void prepare() {
    }
    pll go(ll N, ll K) {
        --K;
        vector<pll> cur;
        cur.emplace_back(-N, 1);
        while (1) {
            map<ll,ll> nxtm;
            for (auto &p : cur) {
                ll x, k;
                tie(x, k) = p;
                x *= -1;
                ll a = (x - 1) / 2;
                ll b = x - 1 - a;
                if (K < k) {
                    return {b, a};
                }
                K -= k;
                if (a > 0) nxtm[-a] += k;
                if (b > 0) nxtm[-b] += k;
            }
            cur = vector<pll>(all(nxtm));
        }
        return {0, 0};
    }
};

mutex mtx;
queue<int> q;

vector<pll> input;
vector<pll> output;

void worker() {
    Solver solver;
    solver.prepare();
    while (1) {
        int id;
        {
            lock_guard<mutex> lock(mtx);
            if (q.empty()) break;
            id = q.front();
            q.pop();
        }
        output[id] = solver.go(input[id].first, input[id].second);
    }
}

int main() {
    const int NUM_THREAD = 7;
    int T;
    cin >> T;
    input.resize(T);
    output.resize(T);
    rep(i, T) {
        cin >> input[i].first >> input[i].second;
    }
    rep(i, T) q.push(i);
    vector<thread> ths(NUM_THREAD);
    for (auto &th : ths) th = thread(worker);
    for (auto &th : ths) th.join();

    rep(i, T) {
        printf("Case #%d: %lld %lld\n", i + 1, output[i].first, output[i].second);
    }
}
