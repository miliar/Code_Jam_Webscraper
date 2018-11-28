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


int main() {
    int T;
    cin >> T;
    for (int C = 1; C <= T; ++C) {
        int n_, Q_;
        cin >> n_ >> Q_;
        const int n = n_, Q = Q_;

        vector<ll> e_(n), s_(n);
        rep(i, n) {
            cin >> e_[i] >> s_[i];
        }
        const auto e = e_, s = s_;

        ll g[128][128];
        clr(g, -1);
        rep(i, n) rep(j, n) {
            cin >> g[i][j];
        }

        const ll inf = ten(18);
        const auto calc_dist = [&](const int start) {
            vector<ll> dp(n, inf);
            using P = pair<ll, int>;
            priority_queue<P, vector<P>, greater<P>> q;
            dp[start] = 0;
            q.push(P(0, start));
            while (!q.empty()) {
                const ll cur_d = q.top().first;
                const ll cur = q.top().second;
                q.pop();

                if (cur_d > dp[cur]) {
                    continue;
                }

                for (int next = 0; next < n; ++next) {
                    if (g[cur][next] != -1) {
                        const ll next_d = cur_d + g[cur][next];
                        if (next_d < dp[next]) {
                            dp[next] = next_d;
                            q.push(P(next_d, next));
                        }
                    }
                }
            }
            return dp;
        };

        vector<ll> recal_g[128];
        rep(i, n) {
            recal_g[i] = calc_dist(i);
        }
        // print2d(recal_g, n, n);

        const auto answer_query = [&](const int start, const int goal) {
            vector<double> dp(n, 1e40);
            using P = pair<double, int>;
            priority_queue<P, vector<P>, greater<P>> q;
            dp[start] = 0;
            q.push(P(0, start));
            while (!q.empty()) {
                const double cur_t = q.top().first;
                const int cur = q.top().second;
                q.pop();

                if (cur_t > dp[cur]) {
                    continue;
                }

                // dump(P(cur_t, cur));

                for (int next = 0; next < n; ++next) {
                    if (e[cur] >= recal_g[cur][next]) {
                        const double next_t = cur_t + double(recal_g[cur][next]) / s[cur];
                        // printf("%d -----> %d\n", cur, next);
                        // dump(recal_g[cur][next]);
                        // dump(s[cur]);
                        // dump(P(next_t, next));
                        // cout << endl;
                        if (next_t < dp[next]) {
                            dp[next] = next_t;
                            q.push(P(next_t, next));
                        }
                    }
                }
            }
            // dump(dp);
            return dp[goal];
        };

        printf("Case #%d:", C);
        rep(q_i, Q) {
            int start, goal;
            cin >> start >> goal;
            --start, --goal;

            const double opt = answer_query(start, goal);
            printf(" %.8f", opt);
        }
        printf("\n");
    }
}
