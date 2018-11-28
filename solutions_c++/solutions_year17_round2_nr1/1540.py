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

ll D, N;
pll H[1005];
int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    int T; cin >> T;
    FOR(Case, 1, T+1) {
        cout << "Case #" << Case << ": ";
        cin >> D >> N;
        REP(i, N) cin >> H[i]._1 >> H[i]._2;
        sort(H, H+N);
        long double k = H[N-1]._1, s = H[N-1]._2;
        for (int i = N-2; i >= 0; --i) {
            long double den = H[i]._2 - s;
            if (den > 0) {
                long double tx = (k - H[i]._1) / den;
                long double kk = H[i]._1 + H[i]._2 * tx;
                if (kk < D) {
                    k = kk;
                    continue;
                }
            }
            k = H[i]._1;
            s = H[i]._2;
        }
        long double a = D / ((D - k) / s);
        REP(i, N)
            amin(a, D / ((D - H[i]._1) / (long double)H[i]._2));
        printf("%.7Lf\n", a);
    }
    return 0;
}

