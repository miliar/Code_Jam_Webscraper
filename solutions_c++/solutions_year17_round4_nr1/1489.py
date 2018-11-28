#define DINGER_GISBAR
#include <bits/stdc++.h>
using namespace std;
const long long MOD = static_cast<int>(1e9) + 7;
//{{{TEMPLATE_BEGIN
#include <unistd.h>
using namespace std::rel_ops;
#ifdef ZEROKUGI
#include <dumper.hpp>
#define dump(x) dumper::dumper(cerr, __LINE__, (#x), (x), 50, 1, 1)
#define tick(...) dumper::tick(__VA_ARGS__)
#pragma message "Compiling " __FILE__
#else
#define dump(x)
#define tick(...)
#endif
typedef long long lint;
typedef unsigned long long ulint;
typedef long double ldouble;
typedef vector<int> vint;
#define rep(i, n) \
    for (int i = 0, i##_len = static_cast<int>(n); i < i##_len; i++)
#define all(c) begin(c), end(c)
#define perm(c)   \
    sort(all(c)); \
    for (bool c##p = 1; c##p; c##p = next_permutation(all(c)))
#define uniquenize(v) (v).erase(unique(all(v)), end(v))
#define cauto const auto&
#define memset(x, y) memset(x, y, sizeof(x))
#define popcount __builtin_popcount
#define gcd __gcd
inline lint bit(int x) { return 1LL << x; }
template <class T>
inline int size(const T& a) {
    return (int)a.size();
}
template <class T>
inline bool chmin(T& a, const T& b) {
    return a > b ? a = b, 1 : 0;
}
template <class T>
inline int clamp(T v, T lo, T hi) {
    return (v > hi) - (v < lo);
}
template <class T>
inline bool chmax(T& a, const T& b) {
    return a < b ? a = b, 1 : 0;
}
template <class T>
inline pair<vector<T>, char> operator*(const vector<T>& v, const char& c) {
    return make_pair(v, c);
}
template <class T>
inline istream& operator>>(istream& is, vector<T>& v) {
#ifdef ZEROKUGI
    if (v.empty()) {
        cerr << "Error L" << __LINE__ << ": vector size is zero." << endl;
        exit(EXIT_FAILURE);
    }
#endif
    for (auto& x : v) is >> x;
    return is;
}
template <class T>
inline ostream& operator<<(ostream& os, const pair<vector<T>, char>& v) {
    bool t = 0;
    for (const T& x : v.first) {
        if (t) os << v.second;
        os << x;
        t = 1;
    }
    return os;
}
template <class T>
inline ostream& operator<<(ostream& os, vector<T>& v) {
    return os << v * ' ';
}
struct before_main {
    before_main() {
        cin.tie(0);
        ios::sync_with_stdio(0);
        cout << fixed << setprecision(20);
        tick(0, 0);
    };
} __before_main;
//}}}TEMPLATE_END

string Case(int x) { return "Case #" + to_string(x) + ": "; }

int n, p, g[101];
int dp[102][102][102][102];
int c[4];

int dfs(int i) {

    if (i == n) {
        rep(z, p) {
            if(z != 0 && c[z] > 0) return 1;
        }
        return 0;
    }

    int& res = dp[i + 1][c[1]][c[2]][c[3]];
    if (res >= 0) return res;

    rep(z, p) {
        int nxt = g[i] + z;
        nxt %= p;
        if (nxt == 0) {
            if (z != 0) c[z]--;
            if (c[z] >= 0) chmax(res, 1 + dfs(i + 1));
            if (z != 0) c[z]++;
        } else {
            if (z != 0) c[z]--;
            c[nxt]++;

            if (c[z] >= 0) chmax(res, dfs(i + 1));

            if (z != 0) c[z]++;
            c[nxt]--;
        }
    }
    return res;
}

void solve() {
    cin >> n >> p;
    rep(i, n) cin >> g[i];
    rep(i, n) g[i] %= p;
    rep(i, p) c[i] = 0;
    memset(dp, -1);
    dp[0][0][0][0] = 0;

    cout << dfs(0) << endl;
}

int main() {
    int test_case;
    cin >> test_case;

    for (int _ = 1; _ <= test_case; _++) {
        cout << Case(_);
        solve();
    }
}
