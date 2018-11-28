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

ll solve(ll n) {
    ll ten[20];
    ten[0] = 1;
    rep(i, 18) ten[i+1] = ten[i] * 10;
    ll res = 0;
    int mini = 0;
    for (int i = 17; i >= 0; --i) {
        for (int d = 9; d >= mini; --d) {
            ll cand = res;
            int j = i;
            while (j >= 0) {
                cand += ten[j] * d;
                --j;
            }
            if (cand <= n) {
                res += ten[i] * d;
                mini = d;
                break;
            }
        }
    }
    return res;
}

mutex mtx;
queue<int> q;
vector<ll> input;
vector<ll> output;

void worker() {
    while (1) {
        int id;
        {
            lock_guard<mutex> lock(mtx);
            if (q.empty()) break;
            id = q.front();
            q.pop();
        }
        output[id] = solve(input[id]);
    }
}

int main() {
    const int NUM_THREAD = 8;
    int T;
    cin >> T;
    input.resize(T);
    output.resize(T);
    rep(i, T) {
        cin >> input[i];
    }
    rep(i, T) q.push(i);
    vector<thread> ths(NUM_THREAD);
    for (auto &th : ths) th = thread(worker);
    for (auto &th : ths) th.join();

    rep(i, T) {
        printf("Case #%d: %lld\n", i + 1, output[i]);
    }
}
