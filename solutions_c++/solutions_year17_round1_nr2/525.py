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
#define cauto const auto &
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

int q[55][55];

struct I {
    int x;
    int k;
    int ev;
};

void solve() {
    int n, p;
    cin >> n >> p;

    vector<int> r(n);
    cin >> r;

    rep(i, n) rep(j, p) cin >> q[i][j];

    vector<I> ii;

    rep(i, n) {
        rep(j, p) {
            //ldouble dm = q[i][j] / (1.1 * r[i]) - 1e-5;
            //ldouble dM = q[i][j] / (0.9 * r[i]) + 1e-5;

            int dm = (10*q[i][j])/(11*r[i]);
            if((10*q[i][j])%(11*r[i]) != 0) dm++;

            int dM = (10*q[i][j])/(9*r[i]);

            //cout << dm << " "  << dM << endl;
            if (dm <= dM) {
                ii.push_back({dm, i, +1});
                ii.push_back({dM, i, -1});
            }
        }
    }

    for(int i = 1; i < 1e6/0.89; i++){
        ii.push_back({i, -1, 0});
    }

    sort(all(ii), [](const I&a, const I&b){
            if(a.x == b.x) return a.ev > b.ev;
            return a.x < b.x;
            });

    vector<int> u(n, 0);
    vector<int> v(n, 0);

    int ans = 0;
    for(auto i: ii) {
        if(i.ev == 0) {
            int x = *min_element(all(u));
            if(x != 0) {
                ans += x;
                rep(j, n) {
                    u[j] -= x;
                    v[j] += x;
                }
            }
        } else if(i.ev == 1) {
            u[i.k]++;
        } else {
            if(v[i.k] > 0) v[i.k]--;
            else u[i.k]--;
        }
    }

    cout << ans << endl;
    /*
        if(ma + 1e-14 < mi) {
            continue;
        }

        if(fabs(mi - lint(mi)) < 1e-14) {
            ans++;
        } else if(lint(mi) != lint(ma)) {
            ans++;
        }
    */
}

int main() {
    int test_case;
    cin >> test_case;

    for(int _ = 1; _ <= test_case; _++) {
        cout << Case(_);
        solve();
    }
}
