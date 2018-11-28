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

vector<string> solve(vector<string> g) {
    int h = g.size();
    int w = g[0].size();
    vector<string> res(h, string(w, ' '));
    rep(ii, 2) {
        rep(jj, 2) {
            rep(i, h) {
                rep(j, w) {
                    if (g[i][j] == '?') continue;
                    char c = g[i][j];
                    int jj = j + 1;
                    while (jj < w && g[i][jj] == '?'){
                        g[i][jj] = c;
                        ++jj;
                    }
                }
            }
            rep(i, h) reverse(all(g[i]));
        }

        vector<string> gg(w, string(h, ' '));
        rep(i, w) rep(j, h) gg[i][j] = g[j][i];
        g = gg;
        swap(h, w);
    }
    return g;
}


int main() {
    int T;
    cin >> T;
    rep(it, T) {
        int h, w;
        cin >> h >> w;
        vector<string> g(h);
        rep(i, h) cin >> g[i];
        vector<string> ans = solve(g);
        printf("Case #%d:\n", it + 1);
        rep(i, h) cout << ans[i] << endl;
    }
}
