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

bool tateyoko[2][114][114], naname[2][114][114];

char query[10000];
int yy[10000];
int xx[10000];

int n, m;
int nanamey[] = {1, 1, -1, -1};
int nanamex[] = {1, -1, 1, -1};
int ttyky[] = {1, 0, -1, 0};
int ttykx[] = {0, 1, 0, -1};

struct hoge{
    char c;
    int y;
    int x;
};


// wakaran

pair<int, vector<hoge>> calc(){
    vector<hoge> ans;
    int score = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            bool ttyk = tateyoko[1][i][j];
            bool nnm = naname[1][i][j];
            if (ttyk) score++;
            if (nnm) score++;

            if (ttyk != tateyoko[0][i][j] || nnm != naname[0][i][j]) {
                char c;
                if (ttyk && nnm)
                    c = 'o';
                else if (ttyk)
                    c = '+';
                else if (nnm)
                    c = 'x';
                ans.push_back({c, i, j});
            }
        }
    }
    return {score, ans};
}

pair<int, vector<hoge>> doit(const vector<int> &yord, const vector<int> &xord) {
    memcpy(tateyoko[1], tateyoko[0], sizeof(tateyoko[0]));
    memcpy(naname[1], naname[0], sizeof(naname[0]));

    for (int i: yord) {
        for (int j: xord) {
            // + ok?
            bool ok1 = true;

            rep(k, 4) {
                int ii = i + nanamey[k];
                int jj = j + nanamex[k];

                while (1 <= ii && ii <= n && 1 <= jj && jj <= n) {
                    ok1 &= !tateyoko[1][ii][jj];
                    ii += nanamey[k];
                    jj += nanamex[k];
                }
            }

            if (ok1) {
                tateyoko[1][i][j] = true;
            }

            // x ok?
            bool ok2 = true;
            rep(k, 4) {
                int ii = i + ttyky[k];
                int jj = j + ttykx[k];

                while (1 <= ii && ii <= n && 1 <= jj && jj <= n) {
                    ok2 &= !naname[1][ii][jj];
                    ii += ttyky[k];
                    jj += ttykx[k];
                }
            }

            if (ok2) {
                naname[1][i][j] = true;
            }
        }
    }
    return calc();
}


void solve() {
    memset(tateyoko, 0);
    memset(naname, 0);

    rep(i, m) {
        string s;
        int y, x;
        cin >> s >> y >> x;
        query[i] = s[0];
        yy[i] = y;
        xx[i] = x;

        if(query[i] == 'o') {
            tateyoko[0][y][x] = true;
            naname[0][y][x] = true;
        }
        if(query[i] == '+') {
            tateyoko[0][y][x] = true;
        }
        if(query[i] == 'x') {
            naname[0][y][x] = true;
        }
    }

    vector<int> y(n), x(n);
    iota(all(y), 1);
    iota(all(x), 1);
    auto ans = doit(y, x);
    pair<int, vector<hoge>> tmp;
    sort(all(y), [](int a, int b){
            int aa = abs(a-n/2);
            int bb = abs(b-n/2);
            if(aa == bb) return a < b;
            return aa < bb;
            });
    tmp = doit(y, x);
    if(ans.first < tmp.first) ans = tmp;

    sort(all(y), [](int a, int b){
            int aa = abs(a-n/2);
            int bb = abs(b-n/2);
            if(aa == bb) return a > b;
            return aa > bb;
            });
    tmp = doit(y, x);
    if(ans.first < tmp.first) ans = tmp;

    sort(all(x), [](int a, int b){
            int aa = abs(a-n/2);
            int bb = abs(b-n/2);
            if(aa == bb) return a > b;
            return aa > bb;
            });
    tmp = doit(y, x);
    if(ans.first < tmp.first) ans = tmp;

    sort(all(x), [](int a, int b){
            int aa = abs(a-n/2);
            int bb = abs(b-n/2);
            if(aa == bb) return a < b;
            return aa < bb;
            });
    tmp = doit(y, x);
    if(ans.first < tmp.first) ans = tmp;
    cout << ans.first << " "  << ans.second.size() << endl;
    for(auto p: ans.second){
        cout << p.c << " "  << p.y << " "  << p.x << endl;
    }
}

int main() {
    int t;
    cin >> t;
    for (int _ = 1; _ <= t; _++) {
        cout << Case(_);

        cin >> n >> m;
        solve();
    }
}
