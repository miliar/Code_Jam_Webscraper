#include <bits/stdc++.h>

#define FORE(i, c) for (auto& i : (c))
#define FOR(i, j, k) for (int i = (j); i < (k); ++i)
#define REP(i, j) FOR(i, 0, j)
#define ALL(v) begin(v), end(v)
#define pb push_back
#define _1 first
#define _2 second
#define vec vector

using namespace std;

typedef long long ll; typedef vec<int> vi; typedef vec<ll> vll; typedef pair<ll, ll> pll; typedef pair<int, int> pii;
template <typename T, typename U> inline void amin(T& x, U y) { if (y < x) x = y; }
template <typename T, typename U> inline void amax(T& x, U y) { if (y > x) x = y; }
template <typename C, typename V> inline bool in(const C& c, const V& v) { return c.find(v) != c.end(); }
template <typename T> inline bool in(const vec<T>& v, const T& t) { return find(ALL(v), t) != end(v); }
template <typename T> inline T sq(T t) { return t * t; }

int N, Q, E[123], S[123], U, V, D[123][123];
long double solve(int p, int h, int d) {
    if (p == V-1) return 0;
    assert(d <= E[h]);
    long double ans = 1e18;
    if (E[h] - d - D[p][p+1] >= 0)
        amin(ans, solve(p+1, h, d + D[p][p+1]) + D[p][p+1] / (long double)S[h]);
    if (E[p] >= D[p][p+1])
        amin(ans, solve(p+1, p, D[p][p+1]) + D[p][p+1] / (long double)S[p]);
    return ans;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    int T; cin >> T;
    FOR(Case, 1, T+1) {
        cout << "Case #" << Case << ": ";
        cin >> N >> Q;
        REP(i, N) cin >> E[i] >> S[i];
        REP(i, N) REP(j, N) cin >> D[i][j];
        cin >> U >> V;
        printf("%.7Lf\n", solve(0, 0, 0));
    }
    return 0;
}

