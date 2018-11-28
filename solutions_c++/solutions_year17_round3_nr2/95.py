#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>
#include <fstream>
#include <bitset>

using namespace std;

#define foreach(it, c) for (__typeof__((c).begin()) it=(c).begin(); it != (c).end(); ++it)
template <typename T> void print_container(ostream& os, const T& c) { const char* _s = " "; if (!c.empty()) { __typeof__(c.begin()) last = --c.end(); foreach (it, c) { os << *it; if (it != last) os << _s; } } }
template <typename T> ostream& operator<<(ostream& os, const vector<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const set<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const multiset<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const deque<T>& c) { print_container(os, c); return os; }
template <typename T, typename U> ostream& operator<<(ostream& os, const map<T, U>& c) { print_container(os, c); return os; }
template <typename T, typename U> ostream& operator<<(ostream& os, const pair<T, U>& p) { os << "(" << p.first << ", " << p.second << ")"; return os; }
template <typename T, std::size_t N> ostream& operator<<(ostream& os, const array<T, N>& c) { print_container(os, vector<T>(c.begin(), c.end())); return os; }

template <typename T> void print(T a, int n, const string& split = " ") { for (int i = 0; i < n; i++) { cerr << a[i]; if (i + 1 != n) cerr << split; } cerr << endl; }
template <typename T> void print2d(T a, int w, int h, int width = -1, int br = 0) { for (int i = 0; i < h; ++i) { for (int j = 0; j < w; ++j) { if (width != -1) cerr.width(width); cerr << a[i][j] << ' '; } cerr << endl; } while (br--) cerr << endl; }
template <typename T> void input(T& a, int n) { for (int i = 0; i < n; ++i) cin >> a[i]; }
#define dump(v) (cerr << #v << ": " << v << endl)

#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
#define erep(i, n) for (int i = 0; i <= (int)(n); ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define clr(a, x) memset(a, x, sizeof(a))
#define sz(a) ((int)(a).size())
#define mp(a, b) make_pair(a, b)
#define ten(n) ((long long)(1e##n))

template <typename T, typename U> void upmin(T& a, const U& b) { a = min<T>(a, b); }
template <typename T, typename U> void upmax(T& a, const U& b) { a = max<T>(a, b); }
template <typename T> void uniq(T& a) { sort(a.begin(), a.end()); a.erase(unique(a.begin(), a.end()), a.end()); }
template <class T> string to_s(const T& a) { ostringstream os; os << a; return os.str(); }
template <class T> T to_T(const string& s) { istringstream is(s); T res; is >> res; return res; }
bool in_rect(int x, int y, int w, int h) { return 0 <= x && x < w && 0 <= y && y < h; }

typedef long long ll;
typedef pair<int, int> pint;
typedef unsigned long long ull;

const double PI = acos(-1);


int main() {
    int T;
    cin >> T;
    for (int C = 1; C <= T; ++C) {
        const int MINS = 24 * 60;

        vector<bool> can_a(MINS + 1, true), can_b(MINS + 1, true);
        {
            int n, m;
            cin >> n >> m;
            rep(i, n) {
                int b, e;
                cin >> b >> e;
                for (int t = b; t < e; ++t) {
                    can_a[t] = false;
                }
            }

            rep(i, m) {
                int b, e;
                cin >> b >> e;
                for (int t = b; t < e; ++t) {
                    can_b[t] = false;
                }
            }
        }

        const int M = 720;
        static int dp[1024][1024][2][2];
        rep(i, 1024) rep(j, 1024) rep(k, 2) rep(first, 2) {
            dp[i][j][k][first] = 1919810;
        }
        if (can_a[0]) {
            dp[0][0][0][0] = 0;
        }
        if (can_b[0]) {
            dp[0][0][1][1] = 0;
        }
        rep(t, MINS) {
            rep(i, min(t, M) + 1) rep(f, 2) rep(first, 2) {
                const int j = t - i;
                assert(j >= 0);

                if (can_a[t]) {
                    upmin(dp[i + 1][j][0][first], dp[i][j][f][first] + (f == 1));
                }
                if (can_b[t]) {
                    upmin(dp[i][j + 1][1][first], dp[i][j][f][first] + (f == 0));
                }
            }
        }

        const int opt = min(min(dp[M][M][0][0], dp[M][M][1][0] + 1), min(dp[M][M][0][1] + 1, dp[M][M][1][1]));
        printf("Case #%d: %d\n", C, opt);
    }
}
